import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ShopService } from './shop.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'instant_shop_front';

  logged = false;
  username = '';
  password = '';

  constructor(private shopService: ShopService,
              public router: Router) {}
  
  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }

  }

  login() {
    this.shopService.login(this.username,this.password).subscribe((data) => {

      localStorage.setItem('token', data.token);

      this.logged = true;
      this.username = '';
      this.password = '';
    });
  }

  logout() {
    this.logged = false
    localStorage.removeItem('token');
  }
}
