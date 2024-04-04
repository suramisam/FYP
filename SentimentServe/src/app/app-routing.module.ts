import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainHomeComponent } from './main-home/main-home.component';
import { FoodPageComponent } from './food-page/food-page.component';
import {HomeComponent} from './home/home.component';
const routes: Routes = [
  {path:'', component:MainHomeComponent},
  {path:'search/:searchTerm', component:HomeComponent},
  {path:'tag/:tag', component:HomeComponent},
  {path:'food/:id', component:FoodPageComponent},
  // {path:'cart-page', component: },
  {path:'main-home', component: MainHomeComponent},
  {path:'food-page', component: HomeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
