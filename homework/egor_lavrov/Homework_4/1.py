my_list = ['red', 'blue', 'green', 'cian', 'yellow']
my_tuple = (1, 'two', 4, 'four', 4)
my_set = {1, 2, 3, 4, 5}
my_dict = {'Alex': 23, 'Kate': 30, 'John': 28, 'Dereck': 29, 'Marry': 26}

''' Для кортежа:
Выведите на экран последний элемент'''
print(my_tuple[-1])

''' Для списка:
1) Добавьте в конец списка еще один элемент.
2) Удалите второй элемент списка'''
my_list.append('white')
my_list.pop(1)

''' Для словаря:
1) Добавьте элемент с ключом ('i am a tuple',) и любым значением.
2) Удалите какой-нибудь элемент'''
my_dict[('i am a tuple',)] = "yes"
my_dict.pop('John')

''' Для множества:
1) Добавьте новый элемент в множество.
2) Удалите элемент из множества'''
my_set.add(6)
my_set.remove(2)

print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)