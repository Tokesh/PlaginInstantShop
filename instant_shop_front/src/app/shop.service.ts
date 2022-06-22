import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthToken, City, Shop } from './models';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShopService {

  BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<AuthToken> {
    return this.http.post<AuthToken>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    });
  }

  getCities(): Observable<City[]> {
    return this.http.get<City[]>(`${this.BASE_URL}/api/cities/`);
  }

  getShops(): Observable<Shop[]> {
    return this.http.get<Shop[]>(`${this.BASE_URL}/api/shops/`);
  }

  getShopsByCity(c_id: number): Observable<Shop[]> {
    return this.http.get<Shop[]>(`${this.BASE_URL}/api/cities/${c_id}/`);
  }

}
