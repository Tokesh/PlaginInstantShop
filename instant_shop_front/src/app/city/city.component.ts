import { Component, OnInit } from '@angular/core';
import { City } from '../models';
import { ShopService } from '../shop.service';

@Component({
  selector: 'app-city',
  templateUrl: './city.component.html',
  styleUrls: ['./city.component.css']
})
export class CityComponent implements OnInit {

  cities: City[] = [];

  constructor(private shopService: ShopService) { }

  ngOnInit(): void {
    this.getCities();
  }

  getCities() {
    this.shopService.getCities().subscribe((data) => {
      this.cities = data;
    })
  }

}
