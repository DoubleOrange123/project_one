import pandas as pd
df = pd.read_csv('C:\\Users\\ultra\\OneDrive\\Desktop\\python\\StudentsPerformance.csv')
df1 = df['gender']
df2 = df[df['gender'] == 'female']
df3 = df[df['gender'] == 'female']

l = []
for i in df['lunch']:
    if i == 'standart':
        l.append(df['lunch'])
print(l)
