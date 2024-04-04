package com.fypbackend.entity;

import jakarta.persistence.*;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@Entity
@Table(name = "restaurantratings")
public class Restaurant {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;
    private String name;
    private Float foodAvaRating;
    private Float priceAvaRating;
    private Float placeAvaRating;
    private Float serviceAvaRating;
    private Float overall;
    private String img;



}
