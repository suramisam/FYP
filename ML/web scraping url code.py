import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_tripadvisor_data(url):
    # Define the headers
    headers = {
        'authority': 'www.tripadvisor.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        # Add other headers as needed
    }
    # Sending a GET request to the URL
    response = requests.get(url, headers=headers)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting restaurant data
        restaurant_data = []

        # Finding all restaurants on the page
        restaurants = soup.find_all('div', class_='geo_wrap')
        print(restaurants)
        geo_names = soup.find_all('div', class_='geo_name')
        print(geo_names)
        for geo_name in geo_names:
            # Find the <a> tag within the div
            a_tag = geo_name.find('a')
            if a_tag:
                # Extract the href attribute
                href = a_tag.get('href')
                href_new = 'https://www.tripadvisor.com/'+ href
                print(href_new)
            else:
                print('Failed to fetch page:', response.status_code)
        df = pd.DataFrame(href_new)
        df.to_excel('tripadvisor_url_data.xlsx', index=False)
        print("Data exported to 'tripadvisor_url_data.xlsx'")
    else:
        print('Failed to fetch page:', response.status_code)
        