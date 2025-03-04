import os
import datetime
import calendar


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(file_path, 'r', encoding='utf-8') as file:
    dates = []
    for line in file.readlines():
        dates.append(datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f'))

one, two, three = dates

print(one + datetime.timedelta(days=7))
print(f'{two.weekday()} - {calendar.day_name[two.weekday()]}')
print((datetime.datetime.now() - three).days)
