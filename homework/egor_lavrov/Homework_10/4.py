'''Дан прайс лист:
При помощи list comprehension и/или dict comprehension превратите этот текст в словарь'''

import re


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_list = re.split(r' |р\n', PRICE_LIST.rstrip('р'))

list_of_items = list(filter(lambda x: x.isdigit() is False, my_list))
list_of_prices = list(map(lambda x: int(x), filter(lambda x: x.isdigit(), my_list)))
my_dict = dict(zip(list_of_items, list_of_prices))
print(my_dict)
