import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

    # Define the headers
headers = {
    'authority': 'www.tripadvisor.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    # Add other headers as needed
}
url = 'https://www.tripadvisor.com/Restaurant_Review-g304142-d11801261-Reviews-Verala-Tangalle_Southern_Province.html'
# Sending a GET request to the URL
response = requests.get(url, headers=headers)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting restaurant data
    restaurantUrl = []

    restaurant_mains = soup.find_all('div', class_='review-container')
    # print(restaurants)
    for restaurant_main in restaurant_mains:
        restaurant_review_main = restaurant_main.find('div', class_='ui_column is-9')
        # print(restaurant_review_main)
        review_spans = restaurant_review_main.find('span', class_='ui_bubble_rating')
        # print(review_spans)
        review_rating = review_spans.get('class')[1]
        # print(review_rating)
        review_date_main = restaurant_review_main.find('div', class_='prw_rup prw_reviews_stay_date_hsx')
        review_date = review_date_main.text
        # print(review_date)
        review_main = restaurant_review_main.find('div', class_='prw_rup prw_reviews_text_summary_hsx')
        review_entry = review_main.find('div', class_='entry')
        review_p_tag = review_entry.find('p', class_='partial_entry')
        review_p_tag_value = review_p_tag.text
        review_span_tag = review_entry.find('span', class_='postSnippet')
        if(review_span_tag!=None):
            review_span_tag_value = review_span_tag.text
            review = review_p_tag_value[:len(review_p_tag_value)-7]  + " " +  review_span_tag_value
        else:
             review = review_p_tag_value
        # print(review)


else:
    print('Failed to fetch page:', response.status_code)

        