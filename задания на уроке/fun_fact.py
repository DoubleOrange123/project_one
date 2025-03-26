def factorial(num:int):
    k = 1 
    for i in range(1,num+1):
        k = i * k
    print (k)

def count(num:int):
    k = 0
    while num != 0:
        k = k + 1
        num = num // 10
    print(k)


def sum(num:int):
    k = 0 
    while num != 0:
        a = num % 10
        k = a + k
        num = num // 10
    print (k)


#Написать функцию, которая находит сумму цифр, кратных 3ём.

def sum_div3(num:int):
    k = 0
    while num != 0:
        a = num % 10 # берет последнюю цифру числа
        num = num // 10 # уменьшает число 
        if a % 3 == 0:
            k = a + k #  суммирует числа
    print (k)


def reverse(num:int):
    k = 0 
    while num != 0:
        a = num % 10
        print (a)
        k = k * 10 + a
        num = num // 10
    print (k)
factorial(7)

