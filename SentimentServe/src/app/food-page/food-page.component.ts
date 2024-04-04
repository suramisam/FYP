import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Food } from '../shared/models/Food';
import {HomeService} from "../home/home.service";
import { FormBuilder } from '@angular/forms';
import {Review} from "../shared/models/Review";

@Component({
  selector: 'app-food-page',
  templateUrl: './food-page.component.html',
  styleUrls: ['./food-page.component.css']
})
export class FoodPageComponent implements OnInit {

  food: Food = new Food();
  reviews: Review[] = [];
  responseObj: any;
  dataParams: any;
  showLoader:boolean = true;
  restaurantDetail: any;
  restaurantReviews: any;
  isAddReviewBtnClick: boolean = false;
  saveReviewForm = this.formBuilder.group({
    review: [null, null]
  });
  constructor(private activatedRoute: ActivatedRoute, private homeService: HomeService, private formBuilder: FormBuilder,
    private router: Router) {
    activatedRoute.params.subscribe((params) => {
      if (params.id){
        this.dataParams = params;
        this.showRestaurantData(this.dataParams);
      }
    });
  }

  ngOnInit(): void {
    // this.homeService.getRestaurantDetails().subscribe(res => {
    //   if(res){
    //     this.responseObj = res;
    //     this.homeService.getRestaurantReviewsById()
    //   }
    // });
  }

  // addToCart(){
  //   this.cartService.addToCart(this.food);
  //   this.router.navigateByUrl('/cart-page');
  // }

  // tslint:disable-next-line:typedef
  addReview(){
    this.isAddReviewBtnClick = true;
  }

  // tslint:disable-next-line:typedef
  onSaveReview(){
    this.isAddReviewBtnClick = true;
    let reqObj: any ={
      "restaurantId": this.food.id,
      "review": this.saveReviewForm.get('review')?.value
    };
    this.homeService.saveAndAnalyseReview(reqObj).subscribe(res=> {
      if(res){
        this.isAddReviewBtnClick = false;
        this.responseObj = res;
        this.showRestaurantData(this.food);
      }
    });
  }

  onCancelReview(){
    this.isAddReviewBtnClick = false;
    this.saveReviewForm.get('review')?.patchValue('');
  }

  showRestaurantData(dataParams: any){
    this.restaurantDetail = this.homeService.getRestaurantDetailById(dataParams.id).subscribe(res => {
      if(res){
        this.showLoader = false;
        this.food.id = res.id;
        this.food.name = res.name;
        this.food.img = res.img;
        this.food.overall = res.overall;
        this.food.foodAvaRating = res.foodAvaRating;
        this.food.placeAvaRating = res.priceAvaRating;
        this.food.priceAvaRating = res.placeAvaRating;
        this.food.serviceAvaRating = res.serviceAvaRating;
        this.getReviewsById(res.id);
      }
    });
  }

  getReviewsById(id: any){
    this.restaurantReviews = this.homeService.getRestaurantReviewsById(id).subscribe(res => {
      if(res){
        this.reviews = res;
      }
    });
  }


}
