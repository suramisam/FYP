import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  constructor(private http: HttpClient) { }

  public getRestaurantDetails(): Observable<any> {
    return this.http.get<any>('http://localhost:8080/restaurant');
  }

  public saveAndAnalyseReview(reqBody: any): Observable<any> {
    return this.http.post("http://localhost:8080/reviews", reqBody);
  }

  public getRestaurantReviewsById(idNumber: any): Observable<any> {
    return this.http.get("http://localhost:8080/reviews/find-all-by-resturant/" + idNumber);
  }

  public getRestaurantDetailById(idNumber: any): Observable<any> {
    return this.http.get<any>("http://localhost:8080/restaurant/by-restaurant-Id/" + idNumber);
  }

}
