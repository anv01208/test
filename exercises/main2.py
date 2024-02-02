import pandas as pd

df = pd.read_csv('data/people.csv')

df = df.set_index(df.Name)


print(df.loc["Alice"])
