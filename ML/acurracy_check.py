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
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import numpy as np
from cleantext import clean


# Load the training data from CSV file
train_df = pd.read_csv(r'D:/Dataset/train_data_aspect_only.csv')

# Vectorize the data using TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=10000)
train_vectors = vectorizer.fit_transform(train_df['Sentence'])

# Train the SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(train_vectors, train_df['Aspect'])

test_df = pd.read_csv(r'D:/Dataset/test_data.csv')
x_test = test_df['Sentence']
y_test = test_df['Aspect']

# Vectorize the new data using the same vectorizer as the training dataS
new_vectors = vectorizer.transform(x_test)

# Predict the aspect labels using the trained SVM model
new_preds = svm_model.predict(new_vectors)


target_names = ['food', 'price', 'place', 'service']
print(y_test)
print(new_preds)
print(target_names)
report = classification_report(y_test, new_preds, target_names=target_names, digits=4, output_dict=True)
report_print = classification_report(y_test, new_preds, target_names=target_names, digits=4)
print(report_print)
