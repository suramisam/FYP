import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

    # Define the headers
headers = {
    'authority': 'www.tripadvisor.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    # Add other headers as needed
}

with open('D:/Dataset/tripadvisor_weligama_rest_url_status__data.csv', 'r', encoding="utf-8", newline='') as file_obj: 

    # Create reader object by passing the file  
    # object to reader method 
    reader_obj = csv.reader(file_obj)
    with open('D:/Dataset/review datasets/tripadvisor_weligama_rest_review_3_data.csv', 'a', encoding="utf-8", newline='') as file_review_data: 
        writer_review_data = csv.writer(file_review_data)
        writer_review_data.writerow(['url','review_rating','review_date','review'])

        with open('D:/Dataset/tripadvisor_weligama_rest_url_status_3_data.csv', 'w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)

            # Iterate over each row in the csv  
            # file using reader object 
            for row in reader_obj: 
                # print(row[1])
                if row[1] == "0":
                    response = requests.get(row[0], headers=headers)
                    print(response)
                    # Checking if the request was successful
                    if response.status_code == 200:
                        # Parsing the HTML content using BeautifulSoup
                        soup = BeautifulSoup(response.text, 'html.parser')
                        writer.writerow([row[0],1])
                        print("Data exported to 'tripadvisor_url_status_data.csv'")
                        # Finding all restaurants on the page
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
                            writer_review_data.writerow([row[0],review_rating,review_date,review])
                    else:
                        writer.writerow([row[0],0])
                        print("Data exported to 'tripadvisor_review_data.csv'")