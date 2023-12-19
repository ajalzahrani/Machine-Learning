import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
num_records = 100

# Features
# Write a np array fuction to generate an array of number from 1 to 12 increase by 0.5
YearsExperience = np.arange(1, 12, 0.5)

# Target variable
Salary = 1000 * YearsExperience

# Create DataFrame
df = pd.DataFrame({
    'YearsExperience': YearsExperience,
    'Salary': Salary
})

# Display the first few rows of the generated data
# print(df.head())
# Save the generated dataset
df.to_csv('FixedSalaryData.csv', index=False)
