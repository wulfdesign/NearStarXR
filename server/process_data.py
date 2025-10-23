import pandas as pd
import numpy as np
import json

# Helper to convert RA/Dec from HMS/DMS to degrees, then radians
def to_radians(s, is_ra=False):
    parts = s.replace('h', ' ').replace('m', ' ').replace('s', ' ').replace('°', ' ').replace("'", ' ').replace('"', ' ').split()
    d, m, s = [float(p) for p in parts]
    decimal = d + m/60 + s/3600
    if is_ra:
        decimal *= 15 # Convert hours to degrees
    return np.deg2rad(decimal)

# Read data and calculate XYZ coordinates
df = pd.read_csv('stars.csv')
df['ra_rad'] = df['RightAscension'].apply(lambda x: to_radians(x, is_ra=True))
df['dec_rad'] = df['Declination'].apply(to_radians)

df['x'] = df['Distance(ly)'] * np.cos(df['dec_rad']) * np.cos(df['ra_rad'])
df['y'] = df['Distance(ly)'] * np.cos(df['dec_rad']) * np.sin(df['ra_rad'])
df['z'] = df['Distance(ly)'] * np.sin(df['dec_rad'])

# Save to JSON
df.to_json('stars.json', orient='records')
print("Processed data and saved to stars.json")

# Run this once: python process_data.py