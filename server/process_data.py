import pandas as pd
import numpy as np
import json
import re
import os

# Get the absolute path of the directory where this script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the full paths for the input and output files
csv_path = os.path.join(script_dir, 'stars.csv')
output_path = os.path.join(script_dir, 'stars.json')


# Helper to convert RA/Dec from HMS/DMS to decimal degrees, then radians
def to_radians(coord_str, is_ra=False):
    # Ensure we are working with a clean string
    s = str(coord_str).strip()

    parts = re.findall(r'[\d.]+', s)
    
    # If the format isn't right, return 0.0
    if len(parts) != 3:
        return 0.0

    # Use non-conflicting variable names
    d_val, m_val, s_val = [float(p) for p in parts]
    
    # Check the original string for the negative sign to determine calculation
    if s.startswith('-'):
        decimal = -d_val - m_val/60 - s_val/3600
    else:
        decimal = d_val + m_val/60 + s_val/3600
        
    if is_ra:
        decimal *= 15 # Convert hours to degrees for Right Ascension
        
    return np.deg2rad(decimal)

# Read data from the CSV file using the full path
# Ensure the columns that should be strings are read as strings
df = pd.read_csv(csv_path, dtype={'RightAscension': str, 'Declination': str})

# Apply the conversion to calculate coordinates in radians
df['ra_rad'] = df['RightAscension'].apply(lambda x: to_radians(x, is_ra=True))
df['dec_rad'] = df['Declination'].apply(to_radians)

# Calculate Cartesian (X, Y, Z) coordinates
df['x'] = df['Distance(ly)'] * np.cos(df['dec_rad']) * np.cos(df['ra_rad'])
df['y'] = df['Distance(ly)'] * np.cos(df['dec_rad']) * np.sin(df['ra_rad'])
df['z'] = df['Distance(ly)'] * np.sin(df['dec_rad'])

# Save the processed data to the JSON file using the full path
df.to_json(output_path, orient='records', indent=4)

print(f"Successfully processed star data and saved to {output_path}")