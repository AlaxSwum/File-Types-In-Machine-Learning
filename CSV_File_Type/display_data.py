import pandas as pd

# Load the CSV file (replace 'your_file.csv' with your actual CSV file path)
df = pd.read_csv('your_file.csv')

# Display the first 5 rows
print(df.head())

# Display the last 5 rows
print(df.tail())

# Display the first 10 rows
print(df.head(10))

# Display the last 10 rows
print(df.tail(10))

