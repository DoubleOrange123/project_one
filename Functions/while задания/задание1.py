#Дано число. Найти его сумму цифр, кратных 3ём. 
#435345
num = int(input())
k = 0
while num != 0:
    i = num % 10
    num = num // 10
    if i % 3 == 0:
        k = k + i
print(k)