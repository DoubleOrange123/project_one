l=[]
l2=[]
l3 =[]
l4 = []
l5 =[]
for i in range(int(input())):
    l.append(int(input()))
for i in range(int(input())):
    l2.append(int(input()))
for i in range (len(l)):
    if l[i] % 2 != 0:
        l3.append(l[i])
for i in range (len(l2)):
    if l2[i] % 2 != 0:
        l3.append(l2[i])
for i in range (len(l)):
    if l[i] % 2 == 0:
        l4.append(l[i])
for i in range (len(l2)):
    if l2[i] % 2 == 0:
        l4.append(l2[i])
print(l3)
print(l4)
for i in range (len(l3)):
    if l4[i] > l3[i]:
        l5.append (l4[i])
print(l5)


 