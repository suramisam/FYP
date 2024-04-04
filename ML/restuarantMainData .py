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
url = 'https://www.tripadvisor.com/Restaurant_Review-g297897-d2053331-Reviews-Black_Coral_Jetwing_Beach-Negombo_Western_Province.html'
# Sending a GET request to the URL
response = requests.get(url, headers=headers)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting restaurant data
    restaurantUrl = []

    restaurant_name = soup.find('h1', class_='HjBfq')
    restaurant_name = restaurant_name.text
    print(restaurant_name)

    restaurant_mains = soup.find('div', class_='hILIJ')
    # print(restaurant_mains);

    restaurant_categories = restaurant_mains.find_all('div', class_='xLvvm ui_column is-12-mobile is-4-desktop')
    # print(restaurant_categories)
    for restaurant_category in restaurant_categories:
        category_div = restaurant_category.find('div', class_='YDAvY R2 F1 e k')
        # print(category_div)
        restaurant_rating_main = category_div.find('div', class_='QEQvp')
        if(restaurant_rating_main!=None):
            # print(restaurant_rating_main)
            restaurant_rating_spans = restaurant_rating_main.find('span', class_='ZDEqb')
            restaurant_rating = restaurant_rating_spans.text
            # print(restaurant_rating)
        attribute_rating_mains = category_div.find_all('div', class_='DzMcu')
        # print(attribute_rating_mains)
        if(len(attribute_rating_mains)!=0):
            for attribute_rating_main in attribute_rating_mains:
                attribute_rating_span = attribute_rating_main.find('span', class_='vzATR')
                attribute_name_span = attribute_rating_main.find('span', class_='BPsyj')
                attribute_name_span_value = attribute_name_span.text
                # attribute_name_rating = attribute_name_span_value + " : " + attribute_rating_span_value
                if(attribute_name_span_value == "Food"):
                    attribute_rating_span_span = attribute_rating_main.find('span', class_='ui_bubble_rating')
                    food_attribute_rating_value =  attribute_rating_span_span.get('class')[1]
                    # print("food_attribute_rating_value" +" : " + food_attribute_rating_value)
                elif(attribute_name_span_value == "Service"):
                    attribute_rating_span_span = attribute_rating_main.find('span', class_='ui_bubble_rating')
                    service_attribute_rating_value =  attribute_rating_span_span.get('class')[1]
                    # print("service_attribute_rating_value"+ " : " + service_attribute_rating_value) 
                elif(attribute_name_span_value == "Value"):
                    attribute_rating_span_span = attribute_rating_main.find('span', class_='ui_bubble_rating')
                    value_attribute_rating_value =  attribute_rating_span_span.get('class')[1]
                    # print("value_attribute_rating_value" +" : "+ value_attribute_rating_value)
                elif(attribute_name_span_value == "Atmosphere"):
                    attribute_rating_span_span = attribute_rating_main.find('span', class_='ui_bubble_rating')
                    atmosphere_attribute_rating_value =  attribute_rating_span_span.get('class')[1]
                    # print("atmosphere_attribute_rating_value" + " : " + atmosphere_attribute_rating_value)     
                
        attribute_details_main = category_div.find('div', class_='UrHfr')
        if(attribute_details_main!=None):
            attribute_detail_type_main = attribute_details_main.find('div', class_='BMlpu')
            if(attribute_detail_type_main!=None):
                attribute_detail_types = attribute_detail_type_main.find_all('div')
                for attribute_detail_type in attribute_detail_types:
                    empty_div = attribute_detail_type.get('class')
                    # print(empty_div)
                    if(empty_div == None):
                        div_title = attribute_detail_type.find('div', class_='tbUiL b').text
                        if(div_title == "CUISINES"):
                            cuisines_attribute = attribute_detail_type.find('div', class_='SrqKb').text
                            cuisines_value = cuisines_attribute
                            # print("cuisines_value" + " : " + cuisines_value)
                        elif (div_title == "Special Diets"):
                            special_diets_value = attribute_detail_type.find('div', class_='SrqKb').text
                            # print("special_diets_value" + " : " + special_diets_value)
                        elif (div_title == "Meals"):
                            meals_value = attribute_detail_type.find('div', class_='SrqKb').text 
                            # print("meals_value" + " : " + meals_value)

        address_attribute_main = category_div.find('div', class_='f e')
        # print(address_attribute_main)
        if(address_attribute_main!=None):
            address_attribute = address_attribute_main.find('div', class_='kDZhm IdiaP')
            # print(address_attribute)
            address_attribute_spans = address_attribute.find_all('span')
            for address_attribute_span in address_attribute_spans:
                empty_span = address_attribute_span.get('class')
                if(empty_span == None):
                    a_address_arribute = address_attribute_span.find('a', class_='YnKZo Ci Wc _S C FPPgD')
                    address_arribute_value = a_address_arribute.find('span', class_='yEWoV').text
                    print("address_arribute_value" + " : " + address_arribute_value)

                    
                    

        


    # with open('D:/Dataset/tripadvisor_anuradhapura_rest_url_data.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     for url in restaurantUrl:
    #         writer.writerow([url])
    #     print("Data exported to 'tripadvisor_url_data.csv'")

else:
    print('Failed to fetch page:', response.status_code)
