import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CartComponent } from './cart/cart.component';
import { CityComponent } from './city/city.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';
import { ProductsComponent } from './products/products.component';
import { ShopsComponent } from './shops/shops.component';
import {AllProductsComponent} from "./all-products/all-products.component";

const routes: Routes = [
  {path: 'cities', component: CityComponent},
  {path: 'cities/:id', component: ShopsComponent},
  {path: 'shops', component: ShopsComponent},
  {path: 'shops/:id/products', component: ProductsComponent},
  {path: 'shops/:s_id/products/:p_id', component: ProductDetailComponent},
  {path: 'cart', component: CartComponent},
  {path: 'all_products', component: AllProductsComponent},
  {path: 'not-found', component: NotFoundComponent},
  {path: '', redirectTo: 'cities', pathMatch: 'full'},
  {path: '**', redirectTo: 'not-found'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
