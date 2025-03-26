l=[]
l2=[]
l3 =[]
l4 = []
numm = (int(input()))
for i in range(int(numm)):
    l.append(int(input()))
    if l[i] % 3 == 0:
        l4.append(l[i])
for i in range(int(numm)):
    l2.append(int(input()))
    if l2[i] % 3 == 0:
        l4.append(l2[i])
for i in range(int(numm)):
    l3.append(int(input()))
    if l3[i] % 3 == 0:
        l4.append(l3[i])
print(l4)