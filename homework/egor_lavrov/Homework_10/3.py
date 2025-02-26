'''Есть функция, которая делает одну из арифметических операций с переданными ей числами
(числа и операция передаются в аргументы функции).
Программа спрашивает у пользователя 2 числа (вне функции)
Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
- если числа равны, то функция calc вызывается с операцией сложения этих чисел
- если первое больше второго, то происходит вычитание второго из певрого
- если второе больше первого - деление первого на второе
- если одно из чисел отрицательное - умножение
'''

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))


def chose_operator(first, second):
    if first < 0 or second < 0:
        operation = '*'
    elif first == second:
        operation = '+'
    elif first > second:
        operation = '-'
    elif second > first:
        operation = '/'
    def inner(func):
        def wrapper(first=first, second=second, operation=operation):
            return func(first, second, operation)
        return  wrapper
    return inner


@chose_operator(first, second)
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second

print(calc())
