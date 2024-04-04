import mysql
import sys
import json
import mysql.connector
# importing python regular expression module
import re
import string
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np
from cleantext import clean

pp=sys.argv[1]
p2 =sys.argv[2]
# restaurantName=sys.argv[3]

# print(pp)
# print(p2)
# print(restaurantName)

stopwords = nltk.corpus.stopwords.words('english')

def stopwords_remove(text_data):
    # Appending words which are not stop words
    removed = [s for s in text_data if s not in stopwords]
    return removed

# Function for tokenization
def tokenization(text_data):
    # Splitting the sentence into words where space is found.
    tokens_text = re.split(' ', text_data)
    return tokens_text


# Function for removing punctuation
def punctuation_remove(text_data):
    # Appending non punctuated words
    punctuation ="".join([t for t in text_data if t not in string.punctuation])
    return punctuation

def emoji_remove(text_data):
    text_data_no_emoji = clean(text_data, no_emoji=True)
    return text_data_no_emoji


paragraph = p2.split('.')
arrayClean=[]

for i, paragraphh in enumerate(paragraph):
  # Add a heading to the paragraph
  sentence_punc = punctuation_remove(paragraphh.strip())
  sentence_no_emoji = emoji_remove(sentence_punc)
  sentence_token = tokenization(sentence_no_emoji)
  stopwords_removed = stopwords_remove(sentence_token)
  sentence = ' '.join(stopwords_removed)
  if(sentence != ''):
    arrayClean.append(sentence)

  print(sentence)
  print(arrayClean)

# Load the training data from CSV file
train_df = pd.read_csv(r'D:/Dataset/train_data_aspect_only.csv')

# Vectorize the data using TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=10000)
train_vectors = vectorizer.fit_transform(train_df['Sentence'])

# Train the SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(train_vectors, train_df['Aspect'])

# Vectorize the new data using the same vectorizer as the training dataS
new_vectors = vectorizer.transform(arrayClean)

# Predict the aspect labels using the trained SVM model
new_preds = svm_model.predict(new_vectors)

data = pd.read_csv(r'D:/Dataset/train_data_rating_only.csv')

# Convert the text into numerical feature vectors using TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['rating']

# Train a Gradient Boosting regression model on the data
gb_regressor = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gb_regressor.fit(X, y)

new_data_vectorized = vectorizer.transform(arrayClean)
new_data_prediction = gb_regressor.predict(new_data_vectorized)

food=[]
price=[]
place=[]
service=[]

mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  password="",
  database="myapp"
)

mycursor = mydb.cursor()
foodSum=0
foodCount=0
priceSum=0
priceCount=0
placeSum=0
placeCount=0
serviceSum=0
serviceCount=0
food_ava_rating=0
price_ava_rating=0
place_ava_rating=0
service_ava_rating=0
foodCurrentRating = 0
priceCurrentRating = 0
placeCurrentRating = 0
serviceCurrentRating = 0

sql = "SELECT COUNT(id) FROM restaurantReviews WHERE food_rating IS NOT NULL AND food_rating > 0 AND restaurant_id =" + str(pp)
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    foodCount = row[0]

print("foodCount: ")
print(foodCount)

sql = "SELECT COUNT(id) FROM restaurantReviews WHERE price_rating IS NOT NULL AND price_rating > 0 AND restaurant_id =" + str(pp)
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    priceCount = row[0]
print("priceCount: ")
print(priceCount)


sql = "SELECT COUNT(id) FROM restaurantReviews WHERE place_rating IS NOT NULL AND place_rating > 0 AND restaurant_id =" + str(pp)
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    placeCount = row[0]
print("placeCount: ")
print(placeCount)

sql = "SELECT COUNT(id) FROM restaurantReviews WHERE service_rating IS NOT NULL AND service_rating > 0 AND restaurant_id =" + str(pp)
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    serviceCount = row[0]
print("serviceCount: ")
print(serviceCount)

for sentence, aspect, rating in zip(arrayClean, new_preds, new_data_prediction):
    print("test")
    if aspect == "food":
        food.append(round(rating, 1));
        print(food)
    elif aspect == "price":
        price.append(round(rating, 1))
        print(price)
    elif aspect == "place":
        place.append(round(rating, 1))
        print(place)
    elif aspect == "service":
        service.append(round(rating, 1))
        print(service)

if(len(food) !=0):
    food_ava_rating = sum(food) / len(food)
if(len(price) !=0):
    price_ava_rating = sum(price) / len(price)
if(len(place) !=0):    
    place_ava_rating = sum(place) / len(place) 
if(len(service) !=0):     
    service_ava_rating = sum(service) / len(service)
sql = "INSERT INTO restaurantreviews (restaurant_id, review, food_rating, price_rating, place_rating, service_rating) VALUES (%s, %s, %s, %s, %s, %s)"
val = (pp, p2, float(round(food_ava_rating,1)), float(round(price_ava_rating,1)), float(round(place_ava_rating,1)), float(round(service_ava_rating,1)))

print("test execute")
mycursor.execute(sql, val)
mydb.commit()


sql = "SELECT food_ava_rating, price_ava_rating, place_ava_rating, service_ava_rating FROM restaurantratings WHERE id =" + str(pp)
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    foodCurrentRating = row[0]
    priceCurrentRating = row[1]
    placeCurrentRating = row[2]
    serviceCurrentRating = row[3]
# print("foodCurrentRating: ")
# print(foodCurrentRating)
# print("priceCurrentRating: ")
# print(priceCurrentRating)
# print("placeCurrentRating: ")
# print(placeCurrentRating)
# print("serviceCurrentRating: ")
# print(serviceCurrentRating)

count=0
averageFoodRating=0.0
averagePriceRating=0.0
averagePlaceRating=0.0
averageServiceRating=0.0
overallReviewRating=0.0

def get_ava_rating(aspectCount, currentRating, newRating ):
    print([aspectCount, currentRating, newRating])
    if newRating==0:
        return currentRating;
    averageAspectRating = ((aspectCount * currentRating) + newRating) / (aspectCount+1)
    print(averageAspectRating)
    return averageAspectRating

averageFoodRating = round(get_ava_rating(foodCount, foodCurrentRating, food_ava_rating),1);
averagePriceRating = round(get_ava_rating(priceCount, priceCurrentRating, price_ava_rating),1);
averagePlaceRating = round(get_ava_rating(placeCount, placeCurrentRating, place_ava_rating),1);
averageServiceRating = round(get_ava_rating(serviceCount, serviceCurrentRating, service_ava_rating),1);

if averageFoodRating !=0:
    count+=1
if averagePriceRating !=0:
    count+=1
if averagePlaceRating !=0:
    count+=1
if averageServiceRating !=0:
    count+=1

if count > 0 :
    overallReviewRating = round((averageFoodRating + averagePriceRating + averagePlaceRating + averageServiceRating) / count, 1)


sql = "UPDATE restaurantratings SET food_ava_rating = %s, price_ava_rating = %s, place_ava_rating = %s, service_ava_rating = %s, overall = %s WHERE id = %s"
val = (float(averageFoodRating), float(averagePriceRating), float(averagePlaceRating),float(averageServiceRating), float(overallReviewRating),pp)
mycursor.execute(sql, val)



# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="myapp"
# )
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO movieratings (name, direction, acting, music, screenplay, overall) VALUES (%s, %s, %s, %s, %s, %s)"
# val = (new_preds[0], 2.3, 2.4, 3.5, 5.3, 2.2)
#
# mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
