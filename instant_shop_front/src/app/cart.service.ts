import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from './models';

@Injectable({
  providedIn: 'root'
})
export class CartService {

  products: Product[] = JSON.parse(localStorage.getItem('cart_products') || '[]');

  addToCart(product: Product) {
    let bool_c:boolean = false;
    this.products = JSON.parse(localStorage.getItem('cart_products') || '[]');
    for(var val of this.products){
      if(val.id == product.id){
        if(product.count==null) product.count=1;
        product.count += 1;
        console.log(product.id, product.count)
        bool_c = true;
        break;
      }
    }
    if(bool_c == false){
      product.count = 1
      this.products.push(product);
    }

    localStorage.setItem('cart_products', JSON.stringify(this.products));
    this.products = JSON.parse(localStorage.getItem('cart_products') || '[]');

  }

  getProducts() {
    return this.products;
  }

  setProducts(products: Product[]) {
    this.products = products;
  }

  removeProduct(product: Product) {
    const removeFirstFoundval = (list: Product[], prod: Product): Product[] => {
      const idx = list.findIndex(object => {
        return object.id === prod.id;
      });

      if (idx === -1) {
          return [...list]
      }

      return list.filter((el, i) => i !== idx)
    };

    this.products = removeFirstFoundval(this.products, product);
    localStorage.setItem('cart_products', JSON.stringify(this.products));
    return this.products;
  }
  updateProduct(product: Product){
    for(var prod of this.products){
      if(prod.id==product.id){
        console.log("ya")
        prod.count += 1
        localStorage.setItem('cart_products', JSON.stringify(this.products));
        this.products = JSON.parse(localStorage.getItem('cart_products') || '[]');
        break;
      }
    }
  }

  clearCart() {
    this.products = [];
    localStorage.removeItem('cart_products')
    return this.products;
  }
  createOrder(product:Product[], name:String, address:String): Observable<any> {
    const headers = { 'content-type': 'application/json'}

    const body=JSON.stringify(product);
    console.log(body, headers)
    return this.http.post('http://127.0.0.1:8000/' + 'api/order/',{'headers':headers, 'name':name, 'address':address, 'prod':body})
  }
  constructor(private http: HttpClient) { }
}
