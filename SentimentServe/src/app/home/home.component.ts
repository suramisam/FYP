import { Component, OnInit } from '@angular/core';

import { Food } from '../shared/models/Food';
import { ActivatedRoute } from '@angular/router';
import {HomeService} from "./home.service";
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  foods: Food[] = [];
  response: any;
  constructor( private route: ActivatedRoute, private homeService: HomeService) { }

  ngOnInit(): void {
    this.homeService.getRestaurantDetails().subscribe(res => {
      if(res){
        this.foods = res;
      }
    });
  }

  // viewRestaurantDetails(food: any){
  //   this.response = food;
  // }

}
