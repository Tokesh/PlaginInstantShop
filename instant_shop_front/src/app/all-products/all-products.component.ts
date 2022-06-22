import { Component, OnInit } from '@angular/core';
import {Category, Product} from "../models";
import {ProductService} from "../product.service";
import {CartService} from "../cart.service";
import {ActivatedRoute, Router} from "@angular/router";
import {Location} from "@angular/common";

@Component({
  selector: 'app-all-products',
  templateUrl: './all-products.component.html',
  styleUrls: ['./all-products.component.css']
})
export class AllProductsComponent implements OnInit {

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

  }

  getProducts() {
    this.route.paramMap.subscribe((params) => {
      this.productService.getAllProducts().subscribe((data) => {
        this.products = data;
        for(var val of this.products){
          val.count = 0
        }
        let cart_prods = JSON.parse(localStorage.getItem('cart_products') || '[]');
        for(var prod of cart_prods){
          this.products[prod.id-1].count = prod.count
        }
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
}
