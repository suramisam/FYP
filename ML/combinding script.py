import os
import pandas as pd

# Directory containing folders with CSV files
root_directory = 'D:/Dataset/review concatenated datasets'

# Initialize an empty list to store DataFrame objects
dfs = []

# Initialize an empty list to store folder names
folder_names = []
print("test")
# Recursively iterate through each file in the root directory and its subdirectories
for root, dirs, files in os.walk(root_directory):
    print("test1")
    for filename in files:
        print("test2")
        if filename.endswith(".csv"):
            print("test3")
            # Read each CSV file into a DataFrame and append to the list
            filepath = os.path.join(root, filename)
            df = pd.read_csv(filepath)
            
            # Extract the folder name
            folder_name = os.path.basename(root)
            folder_names.extend([folder_name]*len(df))  # Extend the list to match the length of the DataFrame
            
            dfs.append(df)

# Concatenate all DataFrames in the list along the rows
combined_df = pd.concat(dfs, ignore_index=True)

# Add a new column for folder names
combined_df['Folder'] = folder_names

# Output the combined DataFrame to a new CSV file
combined_df.to_csv('D:/Dataset/combined dataset.csv', index=False)