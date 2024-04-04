package com.fypbackend.entity;


import jakarta.persistence.*;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "restaurantreviews")
@Data
public class Review {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;
    private Long restaurantId;
    private String review;
    private Float foodRating;
    private Float priceRating;
    private Float placeRating;
    private Float serviceRating;
}
