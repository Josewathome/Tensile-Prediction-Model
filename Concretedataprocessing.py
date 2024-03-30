import pandas as pd
import math
import random
import numpy as np
# Load the CSV file
df = pd.read_csv('concrete_data.csv')

                            # Augmentation of the data
# Number of new samples to generate
num_samples = len(df) * 2

# Generate new samples
bootstrap_samples = df.sample(n=num_samples, replace=True, random_state=1)

# Appendding the new samples to the original dataframe
df = pd.concat([df, bootstrap_samples])

# Reset the index
df.reset_index(drop=True, inplace=True)


                        # Tensile strength Calculation
# Define the cylinder dimensions in mm
diameter = 100
length = 200

# Calculate the tensile strength and add it as a new column
df['Tensile Strength (MPa)'] = (2 * df['Load at Fracture (N)']) / (math.pi * diameter * length)

# Save the updated DataFrame back to the CSV file
df.to_csv('Processed_concrete_data.csv', index=False)
