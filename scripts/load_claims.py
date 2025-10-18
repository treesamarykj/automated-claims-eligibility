import os

import pandas as pd

# checking current path
current_path = os.getcwd()
print("Current path--->",current_path)

# loading the data set
df = pd.read_csv('../data/claims_sample.csv')

#printing the data set
print("Claims--->\n",df)

# inspect the data set
print("Data set shape (row * col)--->",df.shape)
print("Displaying first 2 rows--->\n",df.head(2))
#print("\nSummary:\n", df.describe(include='all'))