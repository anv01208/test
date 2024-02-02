# 26/01/24  'Pandas'

import pandas as pd

data = {
    "key": ["value", "value2"],
    "name": ["Era", "Max"],
    "age": [19, 40]
}

df = pd.DataFrame(data)
df = df.set_index(df.name)

s = pd.Series(
    ['era', 'anuarbekov', '19'],
    name="custom_name",
    index=['name', 'surname', 'age']
)

# print(df)
# print("---------------------")
# print(s)

df2 = pd.read_csv(
    'data/people.csv',
)
# delimiter=';' | sep=';' - разделитель
# header=None (если нет header names)
print(df2)

# print(df2.iloc[:3, 0])  # первые 3 строки - имена
# print("---------------------")
# print(df2.iloc[0:3, 0:2]) # первые 3 строки - имена и возраста
# print("---------------------")
# # : - весь список. Допустим:
# print(df2.iloc[:, 0]) # весь список, только имена









