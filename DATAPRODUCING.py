import pandas as pd
import random

# Define the possible values for each column
cement_types = ['OPC', 'KP Silver', 'WHITE CEMENT']
admixture_types = ['Air-Entraining', None]
cement_water_ratios = [0.45, 0.50, 0.60]
aggregate_sizes = [5, 10, 20]  # in mm
curing_duration =[7]# days
Cement_amount=  [701] # g
Coarse_Aggregate = [2828] # g
Sand_aggregate = [1414] # g

# Define the number of samples
num_samples = 27

# Generate data using list comprehension
data = [[
    i+1,
    random.choice(Cement_amount),  # Cement amount (g)
    random.randint(100, 500),  # Water (g)
    random.choice(cement_types),
    random.choice(aggregate_sizes),
    random.choice(Coarse_Aggregate),
    random.choice(Sand_aggregate),
    random.choice(curing_duration),  # Curing Duration (days)
    random.choice(admixture_types),
    random.randint(50809, 101455),  # Load at Fracture (N)
] for i in range(num_samples)]

# Create DataFrame from generated data
df = pd.DataFrame(data, columns=['Samples', 'Cement amount (g)', 'Water (g)', 'Type of cement', 'Average Aggregate size (mm)', 'Aggregate(Coarse)(g)', 'Aggregate(SAND)(g)','Curing Duration (days)', 'Admixtures', 'Load at Fracture (N)'])

# Save DataFrame to CSV
df.to_csv('concrete_data.csv', index=False)
