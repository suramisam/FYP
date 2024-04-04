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

        geo_names = soup.find_all('div', class_='geo_name')

        for geo_name in geo_names:
            # Find the <a> tag within the div
            a_tag = geo_name.find('a')
            if a_tag:
                # Extract the href attribute
                href = a_tag.get('href')
                href_new = 'https://www.tripadvisor.com/'+ href
                response_restaurant_wise = requests.get(href_new, headers=headers)
                soup_restaurant_wise = BeautifulSoup(response_restaurant_wise.text, 'html.parser')
                restaurantsData = soup_restaurant_wise.find_all('div', class_='Koqnr H I _u DnhEb')
                geoInsideNewDatas = soup_restaurant_wise.find_all('div', class_='uykgT')
                # print(geoInsideNewDatas)
                for geoInsideNewData in geoInsideNewDatas:
                    # Find the <a> tag within the div
                    a_tag_new = geoInsideNewData.find('a')
                    print(a_tag_new)
                    # if a_tag:
                    #     # Extract the href attribute
                    #     href = a_tag.get('href')
                    #     href_new = 'https://www.tripadvisor.com/'+ href
                    #     print(href_new)
                    # else:
                    #     print('Failed to fetch page:', response.status_code)


            else:
                print('Failed to fetch page:', response.status_code)

        # Loop through each restaurant to extract data
        # for restaurant in restaurants:
        #     # Extracting restaurant name
        #     restaurantsLinks = restaurant.find('a', class_='geo_name')
        #     print(restaurantsLinks)
        #     for restaurantLink in restaurantsLinks:
        #         restaurantData = soup.find_all('div', class_='Koqnr H I _u DnhEb')
        #         print(restaurantData)  

        # # Convert data to DataFrame
        # df = pd.DataFrame()

        # # Save DataFrame to Excel file
        # df.to_excel('tripadvisor_data.xlsx', index=False)
        # print("Data exported to 'tripadvisor_data.xlsx'")
        print("Data printed")
    else:
        print('Failed to fetch page:', response.status_code)

# Example usage:
url = 'https://www.tripadvisor.com/Restaurants-g293961-Sri_Lanka.html'
scrape_tripadvisor_data(url)
