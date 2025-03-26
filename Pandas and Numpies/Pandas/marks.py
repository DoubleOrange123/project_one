import pandas as pd

d = {
    'students': ['Karl', 'Monika', 'Jessica'],
    'marks': [4, 5, 3],
    'gender': ['male', 'female', 'male'],
    'age': [18, 20, 19],
    'class': [1, 2, 3]
}
df = pd.DataFrame(d)
df = df.sort_values('age',ascending=False)
df1 = df[(df['marks'] > 4) | (df['class'] == 3)]
print(df1)