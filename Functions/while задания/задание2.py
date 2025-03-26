#Дано число. Проверить является ли оно палиндромом. 
#129


num = int(input())
k = 0 
num2 = num
while num != 0:
    i = num % 10
    num = num // 10
    k = k * 10 + i
print (k)
print (num2)
if k == num2:
    print('да, полиндром')
else:
    print('не полиндром')