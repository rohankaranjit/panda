import pandas as pd

test = pd.read_csv("test.csv")
print(test.info())
print(test.head())
print(test.describe())