import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CartService } from '../cart.service';
import { Category, Product } from '../models';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  products: Product[] = [];
  categories: Category[] = [];
  nameFilter: string = '';

  constructor(private productService: ProductService,
              private cartService: CartService,
              private route: ActivatedRoute,
              private location: Location,
              public router: Router) { }

  ngOnInit(): void {
    this.getProducts();
    this.getCategories();
    this.updateProds();
  }

  getProducts() {
    this.route.paramMap.subscribe((params) => {
      const id = parseInt(params.get('id') || '{}');
      this.productService.getProducts(id).subscribe((data) => {
        this.products = data;
        for(var val of this.products){
          val.count = 0
        }
        let cart_prods = JSON.parse(localStorage.getItem('cart_products') || '[]');
        for(var prod of cart_prods){
          console.log(this.products[prod.id-1])
          console.log(prod)
          this.products[prod.id-1].count = prod.count
        }
      });
    });
  }

  getProductsByCategory(c_id: number) {
    this.route.paramMap.subscribe((params) => {
      const s_id = parseInt(params.get('id') || '{}');
      this.productService.getProductsByCategory(s_id, c_id).subscribe((data) => {
        this.products = data;
        for(var val of this.products){
          val.count = 0
        }

      });
    });
  }

  getCategories() {
    this.route.paramMap.subscribe((params) => {
      const s_id = parseInt(params.get('id') || '{}');
      this.productService.getCategories(s_id).subscribe((data) => {
        this.categories = data;
        console.log(this.categories)
      });
    });
  }
  addToCart(product: Product) {
    this.cartService.addToCart(product);
  }
  plusCounter(product:Product){
    product.count += 1
    this.cartService.updateProduct(product);
  }
  minusCounter(product:Product){
    product.count -= 1
    this.cartService.updateProduct(product);
  }
  goBack() {
    this.location.back();
  }
  updateProds(){

  }

}
