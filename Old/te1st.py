def sum_of_digits_divisible_by_three(number):
    # Преобразуем число в строку, чтобы удобно перебирать каждую цифру
    number_str = str(number)
    sum_digits = 0
    
    # Перебираем каждую цифру в строке
    for digit in number_str:
        if digit.isdigit():  # Проверяем, что символ является цифрой
            int_digit = int(digit)
            if int_digit % 3 == 0:  # Проверяем, кратна ли цифра трем
                sum_digits += int_digit
    
    return sum_digits

# Пример использования функции
number = 123456789
result = sum_of_digits_divisible_by_three(number)
print(f"Сумма цифр, кратных трем, в числе {number}: {result}")