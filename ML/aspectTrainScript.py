import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

from sklearn.metrics import classification_report

# Load the training data from CSV file
train_df = pd.read_csv('D:/Dataset/train_data_aspect_only.csv')

# Vectorize the data using TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=10000)
train_vectors = vectorizer.fit_transform(train_df['Sentence'])

# Train the SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(train_vectors, train_df['Aspect'])

# Load the new data from CSV file
new_data_df = pd.read_csv('D:/Dataset/training_output.csv')

# Vectorize the new data using the same vectorizer as the training dataS
new_vectors = vectorizer.transform(new_data_df['Sentence'])

# Predict the aspect labels using the trained SVM model
new_preds = svm_model.predict(new_vectors)

# Write the predicted aspect labels and sentences to a new CSV file
with open('D:/Dataset/trainOutputAspectWise.csv', 'w', encoding='utf-8') as f:
    f.write("Sentence, Aspect\n")
    # Loop through each sentence and its predicted aspect label
    for sentence, aspect in zip(new_data_df['Sentence'], new_preds):
        # Write the sentence and its predicted aspect label to the output file
        f.write(f"{sentence}, {aspect}\n")

# Print the predicted aspect labels
print(new_preds)
