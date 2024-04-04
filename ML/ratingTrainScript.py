import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np
from sklearn.metrics import mean_squared_error

# Load the data into a pandas dataframe
data = pd.read_csv("D:/Dataset/train_data_rating_only.csv")

# Convert the text into numerical feature vectors using TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['rating']

# Train a Gradient Boosting regression model on the data
gb_regressor = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gb_regressor.fit(X, y)

# Make predictions on a new dataset
new_data = pd.read_csv("D:/Dataset/trainOutputAspectWise.csv")
new_data_vectorized = vectorizer.transform(new_data['Sentence'])
new_data_prediction = gb_regressor.predict(new_data_vectorized)

food=[]
price=[]
place=[]
service=[]

# Write the predicted aspect labels and sentences to a new CSV file
with open('D:/Dataset/training_rating_output.csv', 'w', encoding='utf-8') as f:
    f.write("Sentence, Aspect, Rating\n")
    # Loop through each sentence and its predicted aspect label
    for sentence, aspect, rating in zip(new_data['Sentence'], new_data[' Aspect'], new_data_prediction):
        if aspect == " food":
            food.append(round(rating,1))
        elif aspect== " price":
            price.append(round(rating,1))
        elif aspect== " place":
            place.append(round(rating,1))
        elif aspect== " service":
            service.append(round(rating,1))
        # Write the sentence and its predicted aspect label to the output file
        f.write(f"{sentence}, {aspect}, {rating}\n")

print("New data prediction:", new_data_prediction)


print(food)

count=0
averageFoodRating=0.0
averagePriceRating=0.0
averagePlaceRating=0.0
averageServiceRating=0.0

if len(food) !=0:
    totalFood = np.sum(food)
    averageFoodRating = round(totalFood / len(food), 1)
    print(round(averageFoodRating, 1))
    count+=1
if len(price) !=0:
    totalPrice = np.sum(price)
    averagePriceRating = round(totalPrice / len(price), 1)
    print(round(averagePriceRating, 1))
    count+=1
if len(place) !=0:
    totalPlace = np.sum(place)
    averagePlaceRating = round(totalPlace / len(place), 1)
    print(round(averagePlaceRating, 1))
    count+=1
if len(service) !=0:
    totalService = np.sum(service)
    averageServiceRating = round(totalService / len(service), 1)
    print(round(averageServiceRating, 1))
    count+=1



# totalActing = np.sum(acting)
# averageActRating = round(totalActing / len(acting),1)
# print(round(averageActRating,1))
#
# totalDirection = np.sum(direction)
# averageDirRating = round(totalDirection / len(direction),1)
# print(round(averageDirRating,1))
#
# totalScreenplay = np.sum(screenplay)
# averageScreenRating = round(totalScreenplay / len(screenplay),1)
# print(round(averageScreenRating,1))
#
# totalMusic = np.sum(music)
# averageMusicRating = round(totalMusic / len(music),1)
# print(round(averageMusicRating,1))

totalrestaurant =averageFoodRating+averagePriceRating+averagePlaceRating+averageServiceRating
count2=len(food)+len(price)+len(place)+len(service)
overallReviewRating = round(totalrestaurant / count2, 1)
print(round(overallReviewRating,1))

# with open('D:/Dataset/training_rating_output.csv', 'w', encoding='utf-8') as f:
#     f.write(f"'review_rating', {averageFoodRating}, {averagePriceRating}, {averagePlaceRating}, {averageServiceRating}, {overallReviewRating}\n")

