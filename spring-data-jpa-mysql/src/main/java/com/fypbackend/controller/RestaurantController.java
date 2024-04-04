package com.fypbackend.controller;

import com.fypbackend.dto.ReviewDto;
import com.fypbackend.entity.Restaurant;
import com.fypbackend.entity.Review;
import com.fypbackend.service.RestaurantService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/restaurant")
public class RestaurantController {

    @Autowired
    private RestaurantService restaurantService;

    @CrossOrigin("http://localhost:4200")
    @GetMapping
    public List<Restaurant> findAll() {
        return restaurantService.findAll();
    }

    @CrossOrigin("http://localhost:4200")
    @GetMapping("by-restaurant-Id/{id}")
    public Optional<Restaurant> findById(@PathVariable Long id) {
        return restaurantService.findById(id);
    }

//    // update a book
//    @PutMapping
//    public Review update(@RequestBody Review review) {
//        return projectService.save(review);
//    }
//
//    // delete a book
//    @ResponseStatus(HttpStatus.NO_CONTENT) // 204
//    @DeleteMapping("/{id}")
//    public void deleteById(@PathVariable Long id) {
//        projectService.deleteById(id);
//    }
//
//    @GetMapping("/find/title/{title}")
//    public List<Review> findByTitle(@PathVariable String title) {
//        return projectService.findByTitle(title);
//    }
//
//    @GetMapping("/find/date-after/{date}")
//    public List<Review> findByPublishedDateAfter(
//            @PathVariable @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDate date) {
//        return projectService.findByPublishedDateAfter(date);
//    }

}
