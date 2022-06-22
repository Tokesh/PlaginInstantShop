import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { ProductsComponent } from './products/products.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { ShopsComponent } from './shops/shops.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';
import { CartComponent } from './cart/cart.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { AuthIntercaptor } from './AuthIntercepter';
import { CityComponent } from './city/city.component';
import { AllProductsComponent } from './all-products/all-products.component';

@NgModule({
  declarations: [
    AppComponent,
    ProductsComponent,
    TopBarComponent,
    ShopsComponent,
    ProductDetailComponent,
    CartComponent,
    NotFoundComponent,
    CityComponent,
    AllProductsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthIntercaptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
