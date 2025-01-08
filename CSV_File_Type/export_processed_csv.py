import pandas as pd

# Load the CSV file (replace 'your_file.csv' with your actual CSV file path)
df = pd.read_csv('your_file.csv')

# Save cleaned DataFrame to CSV
df.to_csv('cleaned_data.csv', index=False)

# Save CSV with a different encoding
df.to_csv('cleaned_data.csv', encoding='utf-8-sig')

# Save with semicolon delimiter
df.to_csv('cleaned_data.csv', sep=';')
