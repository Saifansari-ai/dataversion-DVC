# Import required libraries
import pandas as pd
import os

# creating a data dictionary 
data = { 'Name': ['Jai', 'Princi', 'Gaurav'], 
    'Age': [27, 24, 22], 
    'Address': ['Nagpur', 'Nagpur', 'Nagpur']}

# convert dictionary to DataFrame
df = pd.DataFrame(data)

# creating a directory at the root level of the project
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# defining the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# saving the DataFrame to a CSV file
df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")