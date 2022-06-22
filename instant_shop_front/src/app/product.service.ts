import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Category, Product } from './models';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  getProducts(id: number): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.BASE_URL}/api/shops/${id}/products/`);
  }
  getAllProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.BASE_URL}/api/all_products/`);
  }

  getProduct(s_id: number, p_id: number): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.BASE_URL}/api/shops/${s_id}/products/${p_id}/`);
  }

  getCategories(s_id: number): Observable<Category[]> {
    return this.http.get<Product[]>(`${this.BASE_URL}/api/shops/${s_id}/categories/`);
  }

  getProductsByCategory(s_id: number, c_id: number): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.BASE_URL}/api/shops/${s_id}/categories/${c_id}/products/`);
  }

}
