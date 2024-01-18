import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
num_records = 4999

# Features
square_feet = np.random.randint(1000, 3000, size=num_records)
num_bedrooms = np.random.randint(1, 5, size=num_records)
num_bathrooms = np.random.uniform(1, 4, size=num_records)
year_built = np.random.randint(1950, 2023, size=num_records)
neighborhoods = np.random.choice(
    ['Suburban', 'Urban', 'Rural'], size=num_records)
garage_spaces = np.random.randint(0, 3, size=num_records)
lot_size = np.random.uniform(0.1, 1.0, size=num_records)
# Cities
cities = np.random.choice(
    ['New York', 'Los Angeles', 'Kansas City', 'Houston'], size=num_records)

# Target variable
price = 100000 * square_feet + 50000 * num_bedrooms + 75000 * num_bathrooms + \
    5000 * (2023 - year_built) + 20000 * \
    garage_spaces + 5000 * (lot_size * 1000)

# Create DataFrame
df = pd.DataFrame({
    'Square Feet': square_feet,
    'Number of Bedrooms': num_bedrooms,
    'Number of Bathrooms': num_bathrooms,
    'Year Built': year_built,
    'Neighborhood': neighborhoods,
    'Garage Spaces': garage_spaces,
    'Lot Size': lot_size,
    'City': cities,
    'Price': price
})

# Display the first few rows of the generated data
# print(df.head())
# Save the generated dataset
df.to_csv('housingDataGen.csv', index=False)
