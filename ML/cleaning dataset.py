import nltk
import re
import string
import csv
from cleantext import clean
import numpy as np

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Get English stopwords
stopwords = nltk.corpus.stopwords.words('english')

def stopwords_remove(text_data):
    # Appending words which are not stopwords
    removed = [word for word in text_data if word.lower() not in stopwords]
    return removed

def tokenization(text_data):
    # Split the sentence into words using NLTK's word tokenizer
    tokens_text = nltk.word_tokenize(text_data)
    return tokens_text

def punctuation_remove(text_data):
    # Remove punctuation using regex
    text_data_no_punct = re.sub('['+string.punctuation+']', '', text_data)
    return text_data_no_punct

def emoji_remove(text_data):
    text_data_no_emoji = clean(text_data, no_emoji=True)
    return text_data_no_emoji

# # Open the input file for reading
# with open('input.txt', 'r', encoding='utf-8') as f:
#     # Read the contents of the file into a variable
#     text = f.read()

# paragraphs = text.split('.')

# with open('output.csv', 'w', encoding='utf-8') as f:
#     f.write("Sentence\n")
#     # Loop through each paragraph
#     for i, paragraph in enumerate(paragraphs):
#         # Remove punctuation
#         sentence_no_punct = punctuation_remove(paragraph.strip())
#         # Tokenize the sentence
#         sentence_tokens = tokenization(sentence_no_punct)
#         # Remove stopwords
#         stopwords_removed = stopwords_remove(sentence_tokens)
#         # Join the words back into a sentence
#         sentence = ' '.join(stopwords_removed)
#         # Write the processed sentence to the output file
#         f.write(sentence + '\n')

with open('D:/Dataset/combined dataset testing.csv', 'r', encoding="utf-8", newline='') as file_obj: 
    reader_obj = csv.reader(file_obj)
    next(reader_obj, None)
    with open('D:/Dataset/review only sentence dataset.csv', 'w', encoding="utf-8", newline='') as file_review_data:
        writer_review_data = csv.writer(file_review_data)
        writer_review_data.writerow(['review_sentence'])
        # writer_review_data.writerow(['url','review_rating','review_date','original review','folder','Review Sentence'])
        for row in reader_obj:
            # print(row[3])
            sentence_no_punct = punctuation_remove(row[3].strip())
            # print(sentence_no_punct)
            sentence_no_emoji = emoji_remove(sentence_no_punct)
            # print(sentence_no_emoji)
            # Tokenize the sentence
            sentence_tokens = tokenization(sentence_no_emoji)
            # print(sentence_tokens)
            # # # Remove stopwords
            stopwords_removed = stopwords_remove(sentence_tokens)
            # print(stopwords_removed)
            # # Join the words back into a sentence
            sentence = ' '.join(stopwords_removed)
            # print(sentence)
            # Write the processed sentence to the output file
            # writer_review_data.writerow(row.append(sentence))
            # writer_review_data.writerow(np.concatenate((row, [sentence])))
            writer_review_data.writerow([sentence])

print("Processing complete.")



