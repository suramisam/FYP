package com.fypbackend.service;

import com.fypbackend.entity.Restaurant;
import com.fypbackend.entity.Review;
import com.fypbackend.repository.RestaurantRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.List;
import java.util.Optional;

@Service
public class RestaurantService {
    @Autowired
    private RestaurantRepository restaurantRepository;

    public List<Restaurant> findAll() {

        return restaurantRepository.findAll();
    }

    public Optional<Restaurant> findById(Long id) {

        return restaurantRepository.findById(id);
    }

    public void deleteById(Long id) {
        restaurantRepository.deleteById(id);
    }

//    public List<Review> findByTitle(String title) {
//        return projectRepository.findByTitle(title);
//    }
//
//    public List<Review> findByPublishedDateAfter(LocalDate date) {
//        return projectRepository.findByPublishedDateAfter(date);
//    }
}
