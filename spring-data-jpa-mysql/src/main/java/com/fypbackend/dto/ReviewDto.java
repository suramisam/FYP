package com.fypbackend.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ReviewDto {
    private Long restaurantId;
    private String review;
}
