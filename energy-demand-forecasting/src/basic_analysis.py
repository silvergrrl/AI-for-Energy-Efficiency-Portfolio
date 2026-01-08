
import pandas as pd
import matplotlib.pyplot as plt

# Download and load the dataset (replace with actual file path or URL)
# Example: 'http://traces.cs.umass.edu/data/smart/smartdata.csv'
data_url = 'YOUR_DATASET_URL_OR_PATH.csv'
df = pd.read_csv(data_url)

# Display basic info
print("Dataset shape:", df.shape)
print("Columns:", df.columns)
print(df.head())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Convert timestamp column to datetime (replace 'timestamp' with actual column name)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Plot energy consumption over time for one home (replace 'home_id' and 'energy' as needed)
home_id = 1
df_home = df[df['home_id'] == home_id]
plt.figure(figsize=(12, 6))
plt.plot(df_home.index, df_home['energy'])
plt.title(f'Energy Consumption Over Time - Home {home_id}')
plt.xlabel('Time')
plt.ylabel('Energy (kWh)')
plt.show()

# Explore correlation with temperature (replace 'temperature' as needed)
plt.scatter(df_home['temperature'], df_home['energy'], alpha=0.5)
plt.title(f'Energy vs Temperature - Home {home_id}')
plt.xlabel('Temperature (°C)')
plt.ylabel('Energy (kWh)')
plt.show()
