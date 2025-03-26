import pandas as pd
df = pd.read_csv('C:\\Users\\ultra\\OneDrive\\Desktop\\task\\world-data-2023.csv')
print(df.head(5))
print(df.loc[0])
df1 = df[['Country','Land Area(Km2)']]
print(df.nunique())
print(df1.sort_values(by=['Land Area(Km2)'],ascending=False))
for i in df1['Land Area(Km2)']:
    i = (str(i))

