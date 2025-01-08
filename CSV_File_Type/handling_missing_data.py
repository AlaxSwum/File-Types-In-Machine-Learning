import pandas as pd

# Load the CSV file (replace 'your_file.csv' with your actual CSV file path)
df = pd.read_csv('your_file.csv')

# Check for missing values
print(df.isnull().sum())  # Show the count of missing values per column

# Fill missing values with 0
df.fillna(0, inplace=True)

# Fill missing values with the mean of a column
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Fill missing values with a custom string
df['column_name'].fillna('Unknown', inplace=True)

# Drop rows where any column has missing values
df.dropna(inplace=True)

# Drop rows where all columns have missing values
df.dropna(how='all', inplace=True)

# Drop columns with missing values
df.dropna(axis=1, inplace=True)

# Sort rows by a specific column in ascending order
df_sorted = df.sort_values(by='column_name')

# Sort in descending order
df_sorted_desc = df.sort_values(by='column_name', ascending=False)

# Sort by multiple columns
df_sorted_multi = df.sort_values(by=['col1', 'col2'], ascending=[True, False])

# Group data by a column and calculate mean
grouped = df.groupby('category_column').mean()

# Group by a column and calculate sum
summed = df.groupby('category_column').sum()

# Group and apply multiple aggregation functions
agg = df.groupby('category_column').agg({'col1': 'sum', 'col2': 'mean'})

# One-hot encode categorical column
encoded_df = pd.get_dummies(df, columns=['category_column'])

# Encode categorical column without adding column prefix
encoded_df = pd.get_dummies(df, columns=['category_column'], prefix='', prefix_sep='')
