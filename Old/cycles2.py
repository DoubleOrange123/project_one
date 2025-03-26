numm = int(input())
summ = 0 
summ2 = 0
l =[]
l2 = []
for i in range(numm):
    l.append(int(input('ввод первый список закончен '))) 
for i in range(numm):
    l2.append(int(input('ввод второй список закончен ')))
for i in range(len(l)):
    summ = summ + l[i] 
for i in range (len(l2)):
    summ2 = summ2 + l2[i]
if summ > summ2:
    print (summ)
else:
    print(summ2)
