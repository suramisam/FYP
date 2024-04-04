export class Review{
  id!:number;
  restaurantId!: number;
  review!: string;
  foodRating:number = 0;
  priceRating:number = 0;
  placeRating:number = 0;
  serviceRating:number = 0;
}
