import csv

with open('D:/Dataset/new.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        print("Data exported to 'new.csv'")