import { Food } from "./Food";

export class CartItem{
    constructor(food:Food){
      this.food = food;
    }
    food:Food;
}
