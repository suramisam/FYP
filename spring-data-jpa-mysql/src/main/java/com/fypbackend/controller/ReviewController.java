package com.fypbackend.controller;

import com.fypbackend.dto.ResponseDto;
import com.fypbackend.dto.ReviewDto;
import com.fypbackend.entity.Restaurant;
import com.fypbackend.entity.Review;
import com.fypbackend.service.RestaurantService;
import com.fypbackend.service.ReviewService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;

@RestController
@RequestMapping("/reviews")
public class ReviewController {
    @Autowired
    ReviewService reviewService;

//    @GetMapping
//    public List<Review> findAllReviewsByRestaurantId() {
//        return reviewService.findAll();
//    }

    @CrossOrigin("http://localhost:4200")
    @GetMapping("find-all-by-resturant/{restaurantId}")
    public List<Review> findAllByRestaurantId(@PathVariable Long restaurantId) {
        return reviewService.findAllReviewsByRestaurantId(restaurantId);
    }

    // create a book
    @ResponseStatus(HttpStatus.CREATED) // 201
    @CrossOrigin("http://localhost:4200")
    @PostMapping
    public ResponseDto create(@RequestBody ReviewDto reviewDto) throws IOException, InterruptedException {

        return reviewService.save(reviewDto.getRestaurantId(), reviewDto.getReview());
    }
}
