package com.fypbackend.repository;

import com.fypbackend.entity.Review;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface ReviewRepository extends JpaRepository<Review, Long> {


    List<Review> findByRestaurantId(Long restaurantId);
}
