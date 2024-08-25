import pandas as pd

df = pd.read_csv("data/titanic.csv")
df = df.dropna()
df = df.drop_duplicates()
df.to_csv('data/titanic_processed.csv', index=False)
# print(df.describe())