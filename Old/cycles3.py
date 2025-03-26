l=[]
numm = int(input())
for i in range(numm):
    l.append(int(input()))
for i in range(numm):
    if i % 2 != 0:
       l[i] =  l[i] * (-1)
print(l)