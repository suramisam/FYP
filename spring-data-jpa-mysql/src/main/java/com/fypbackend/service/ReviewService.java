package com.fypbackend.service;

import com.fypbackend.dto.ResponseDto;
import com.fypbackend.entity.Restaurant;
import com.fypbackend.entity.Review;
import com.fypbackend.repository.RestaurantRepository;
import com.fypbackend.repository.ReviewRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.List;
import java.util.Optional;

@Service
public class ReviewService {

    @Autowired
    private ReviewRepository reviewRepository;

    @Autowired
    private RestaurantRepository restaurantRepository;

//    public List<Review> findAll() {
//        return reviewRepository.findAll();
//    }
    public List<Review> findAllReviewsByRestaurantId(Long restaurantId) {
        return reviewRepository.findByRestaurantId(restaurantId);
    }
    public ResponseDto save(Long restaurantId, String review) throws IOException, InterruptedException {

        String[] cmd = {
                "python",
                "D:/Dataset/MLOverAllScript.py",
                Long.toString(restaurantId),
                review
        };
        Runtime.getRuntime().exec(cmd);
        Thread.sleep(3000);
        ResponseDto responseDto = new ResponseDto();
        responseDto.setStatus("Success");
        return responseDto;
    }
}