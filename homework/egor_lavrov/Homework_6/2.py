'''Напишите программу, которая перебирает последовательность от 1 до 100.
Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа,
а для чисел кратных 5 печатать "Buzz".
Для чисел которые кратны одновременно и 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.'''

for num in range(1, 101):
    if (num % 3 == 0) and (num % 5 == 0):
        print('FuzzBuzz')
    elif (num % 3 == 0):
        print('Fuzz')
    elif (num % 5 == 0):
        print('Buzz')
    else:
        print(num)
