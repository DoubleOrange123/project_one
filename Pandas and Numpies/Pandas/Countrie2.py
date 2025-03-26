import pandas as pd
df = pd.read_csv('C:\\Users\\ultra\\OneDrive\\Desktop\\task\\travel insurance.csv')
print(df.info())
print(df.loc[0]) #женщины до 40, мужчины больше 45

df1 = df[(df['Gender'] == 'M') & (df['Age'] > 45 ) | (df['Gender'] == 'F') & (df['Age'] < 40 )] 
#print(len(df1))
#топ 3 агнеств по коммисии в оффлайн режиме 

df5 = df[df['Distribution Channel'] == 'Offline']
#print(df5)
df6 = df5.sort_values('Commision (in value)',ascending=False)
#print(df6.head(3))

#df4 = df[df['Distribution Channel'] == 'Offline'] [['Agency','Commision (in value)']]
#print(df4)

#страна норвегия или италия продукт нейм меньше 11 символов

df7 = [(df['Destination'] == 'Norway') & (df['Product Name'] < 11)] | [(df['Destination'] == 'Italy') & (df['Product Name'] < 11)]
print(len(df7))
