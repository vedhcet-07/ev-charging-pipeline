import kagglehub
import pandas as pd
import numpy as np
import os

# Download dataset
path = kagglehub.dataset_download(
    "vivekattri/global-ev-charging-stations-dataset"
)

# Locate CSV
files = os.listdir(path)

csv_file = None

for file in files:
    if file.endswith('.csv'):
        csv_file = file
        break

csv_path = os.path.join(path, csv_file)

# Read dataset
df = pd.read_csv(csv_path)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna('Unknown', inplace=True)
    else:
        df[col].fillna(df[col].median(), inplace=True)

# Feature Engineering
df['High Usage Station'] = df['Usage Stats (avg users/day)'].apply(
    lambda x: 1 if x > 50 else 0
)

# Save processed file
df.to_csv('processed_ev_data.csv', index=False)

print('ETL Pipeline Executed Successfully')
