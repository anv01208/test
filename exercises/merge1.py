import pandas as pd

data1 = {
    'name': ['Max', 'Aray', 'Yerbol'],
    'age': [12, 20, 35]
}

data2 = {
    'name': ['Sasha', 'Aray', 'Yerbol'],
    'gender': ['Male', 'Female', 'Male']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print('======================')
print(df2)

res = pd.merge(df1, df2, how='outer')
print('=========res=========')
print(res)








