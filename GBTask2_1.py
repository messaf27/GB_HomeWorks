# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

number = input('Введите вещественное число: ')
# проверка на знак.
if '.' in number:
    number = number.replace('.', '')
elif ',' in number:
    number = number.replace(',', '')

number = int(number)
sum = 0
mult = 1
 
while number > 0:
    digit = number % 10
    sum = sum + digit
    mult = mult * digit
    number = number // 10

print(f'Сумма цыфр в числе: {sum}')