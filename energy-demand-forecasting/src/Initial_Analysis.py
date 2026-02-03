import pandas as pd
import tarfile
import os

# Unpack the dataset if needed
data_dir = '../data'
tar_path = os.path.join(data_dir, 'apartment-electrical.tar.gz')
with tarfile.open(tar_path, 'r:gz') as tar:
    tar.extractall(path=data_dir)

# Load the electrical data
electrical_csv = os.path.join(data_dir, 'apartment-electrical.csv')
df_elec = pd.read_csv(electrical_csv)

# Load the weather data
weather_csv = os.path.join(data_dir, 'apartment-weather.csv')
df_weather = pd.read_csv(weather_csv)

# Basic exploration
print("Electrical data shape:", df_elec.shape)
print("Electrical columns:", df_elec.columns)
print(df_elec.head())

print("Weather data shape:", df_weather.shape)
print("Weather columns:", df_weather.columns)
print(df_weather.head())

# Check for missing values
print("Missing values in electrical data:\n", df_elec.isnull().sum())
print("Missing values in weather data:\n", df_weather.isnull().sum())

# Save a small sample for GitHub
sample_elec = df_elec.sample(n=100)
sample_elec.to_csv(os.path.join(data_dir, 'apartment-electrical-sample.csv'), index=False)