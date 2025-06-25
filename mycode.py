# Import required libraries
import pandas as pd
import os

# creating a data dictionary 
data = { 'Name': ['Jai', 'Princi', 'Gaurav'], 
    'Age': [27, 24, 22], 
    'Address': ['Nagpur', 'Nagpur', 'Nagpur']}

# convert dictionary to DataFrame
df = pd.DataFrame(data)

# Add new line in the existing DataFrame
new_data = {'Name' : 'saif', 'Age' : 22, 'Address': 'Lucknow'}
df.loc[len(df)] = new_data

# Add another new line in the existing dataframe
new_data_2 = {'Name': 'Ankit','Age':23,'Address':'Delhi'}
df.loc[len(df)] = new_data_2

# creating a directory at the root level of the project
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# defining the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# saving the DataFrame to a CSV file
df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")