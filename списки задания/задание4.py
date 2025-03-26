#Дан список чисел.
#Найти количество трёхзначных чисел, оканчивающихся на 4.

l=[]
l2 =[]
numm = (int(input()))
for i in range(numm):
    l.append(int(input()))
    if l[i] >= 100 and l[i] <= 999 and l[i] % 10 == 4:
        l2.append(l[i])
print (l2)
