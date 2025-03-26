#Дано число. Проверить является ли оно палиндромом. 




def palindrom (num:int):
    a=0
    while num != 0:
        k = num % 10
        print (k)
        num = num // 10
        a = a + k
    print (a)

palindrom(143234)