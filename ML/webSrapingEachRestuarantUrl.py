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
url = 'https://www.tripadvisor.com/Restaurants-g304132-Anuradhapura_North_Central_Province.html'
# Sending a GET request to the URL
response = requests.get(url, headers=headers)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting restaurant data
    restaurantUrl = []

    # Finding all restaurants on the page
    restaurants = soup.find_all('div', class_='Koqnr H I _u DnhEb')
    # print(restaurants)
    geo_names = soup.find_all('div', class_='uykgT')
    # print(geo_names)
    for geo_name in geo_names:
        # Find the <a> tag within the div
        a_tag = geo_name.find('a')
        if a_tag:
            # Extract the href attribute
            href = a_tag.get('href')
            href_new = 'https://www.tripadvisor.com'+ href
            # print("restaurant 1111111"+ href_new)
            restaurantUrl.append(href_new)
            print( restaurantUrl)
        else:
            print('Failed to fetch page:', response.status_code)
    with open('D:/Dataset/tripadvisor_anuradhapura_rest_url_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for url in restaurantUrl:
            writer.writerow([url])
        print("Data exported to 'tripadvisor_url_data.csv'")

else:
    print('Failed to fetch page:', response.status_code)
