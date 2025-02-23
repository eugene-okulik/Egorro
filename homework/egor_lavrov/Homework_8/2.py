'''Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число'''


def fib(limit=100):
    a, b, count = 0, 1, 1
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


needed_positions = [5, 200, 1000, 100000]
count = 1

for number in fib(needed_positions[-1] + 1):
    if count in needed_positions:
        print(f'{count}-е число: {number}')
    count += 1
