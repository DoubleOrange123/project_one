l=[]
l2=[]
l3=[]
numm = int(input())
numm2 = int(input())
numm3 = numm + numm2
for i in range(numm):
    l.append(int(input('ввод первый список')))
for i in range (numm2):
    l2.append(int(input('ввод второй список')))
for i in range (len(l)):
    l3.append([l[i],l2[i]])
print(l3)