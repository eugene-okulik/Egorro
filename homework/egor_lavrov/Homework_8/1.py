import random

'''Есть две переменные, salary и bonus. Salary - int, bonus - bool.
Спросите у пользователя salary. А bonus пусть назначается рандомом.
Если bonus - true, то к salary должен быть добавлен рандомный бонус.

Примеры результатов:

10000, True - '$10255'
25000, False - '$25000'
600, True - '$3785' '''

salary = int(input('Введите размер заработной платы\n'))
bonus = random.choice([True, False])

if bonus is True:
    plus = salary + random.randint(1, salary)
    print(f"{salary}, {bonus} - '${plus}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
