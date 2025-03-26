import pandas as pd
df = pd.read_csv('C:/Users/ultra/OneDrive/Desktop/pandas files/ratings.csv', encoding='CP866')
df1 = df[df['num_rating']>2.5][['coffee_shop_name','num_rating']].drop_duplicates()
print(df1)
df2 = df1[:21]
print(df2)
df3 = df1.tail(20)
print(df3)
df4 = df1.sort_values(by = ['num_rating'])
print(df4)
