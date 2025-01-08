import pandas as pd

# Read CSV file
df = pd.read_csv('data.csv')  

# Load CSV with a custom separator
df_semicolon = pd.read_csv('data.csv', sep=';')

# Load only specific columns
df_cols = pd.read_csv('data.csv', usecols=['Name', 'Salary'])

# Load the first 50 rows only
df_small = pd.read_csv('data.csv', nrows=50)

# Skip the first row and give custom column names
df_custom = pd.read_csv('data.csv', header=None, names=['ID', 'Name', 'Age', 'Score'])

# Save DataFrame to CSV
df.to_csv('output.csv')

# Save CSV without the row index
df.to_csv('output.csv', index=False)

# Save only specific columns
df.to_csv('output.csv', columns=['Name', 'Salary'], index=False)

# Save with custom missing value placeholder
df.to_csv('output.csv', na_rep='Missing')

# Append new rows to an existing CSV
df.to_csv('output.csv', mode='a', header=False)

# Save CSV with semicolon as delimiter
df.to_csv('output.csv', sep=';')