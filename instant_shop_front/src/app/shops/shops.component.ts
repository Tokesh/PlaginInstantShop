import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Shop } from '../models';
import { ShopService } from '../shop.service';

@Component({
  selector: 'app-shops',
  templateUrl: './shops.component.html',
  styleUrls: ['./shops.component.css']
})
export class ShopsComponent implements OnInit {

  shops: Shop[] = [];

  constructor(private shopService: ShopService,
              private route: ActivatedRoute,
              private router: Router,
              private location: Location) { }

  ngOnInit(): void {
    if (this.router.url === '/shops') {
      this.getShops();
    }
    else {
      this.getShopsByCity();
    }
  }

  getShops() {
    this.shopService.getShops().subscribe((data) => {
      this.shops = data;
    })
  }

  getShopsByCity() {
    this.route.paramMap.subscribe((params) => {
      const c_id = parseInt(params.get('id') || '{}');
      this.shopService.getShopsByCity(c_id).subscribe((data) => {
        this.shops = data;
      })
    })
  }

  goBack() {
    this.location.back();
  }

}
