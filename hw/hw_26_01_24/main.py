import pandas as pd

df = pd.read_csv('people.csv')

NameAndAge = df[['Name', 'Age']]

NameAndAge.to_csv('people_2.csv', index=False)
