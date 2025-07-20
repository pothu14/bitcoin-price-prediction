import pandas as pd

# Load the dataset
df = pd.read_csv("bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")

# Convert UNIX timestamp to readable datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

# Drop rows where all price values are missing or zero
df.dropna(subset=['Open', 'High', 'Low', 'Close', 'Weighted_Price'], how='all', inplace=True)
df = df[(df[['Open', 'High', 'Low', 'Close', 'Weighted_Price']] != 0).any(axis=1)]

# Fill missing values using forward fill
df.ffill(inplace=True)


# Add time-based features
df['Date'] = df['Timestamp'].dt.date
df['Year'] = df['Timestamp'].dt.year
df['Month'] = df['Timestamp'].dt.month
df['Hour'] = df['Timestamp'].dt.hour

# Save the cleaned file
df.to_csv("bitcoin_cleaned.csv", index=False)

print("✅ Cleaned dataset saved as bitcoin_cleaned.csv")



