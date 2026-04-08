import os
import re
import argparse
from colorama import init, Fore, Style


init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to the log file or directory with logs")
parser.add_argument("-w", "--word", help="Word for search")
parser.add_argument("--full", help="Print full log message", action="store_true")
args = parser.parse_args()
print(args.file, args.word, args.full)

logs_folder_path = args.file

if logs_folder_path.endswith('.log') or logs_folder_path.endswith('.txt'):
    list_of_log_files = []
    list_of_log_files.append(logs_folder_path)
else:
    list_of_log_files = os.listdir(logs_folder_path)

if args.word is None:
    text_to_search = input('Какое слово нужно найти?\n')
else:
    text_to_search = args.word

print(f'args.file= {args.file}')
print(type(args.word))


count = 0
print(f'Папка с логами:\n{logs_folder_path}\n')
print(f'Файлов в папке: {len(list_of_log_files)}\n')


# Делим файл на блоки и создаём из них словарь
def make_dict(text):
    pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}'
    dist_keys = re.findall(pattern, text)
    parts = re.split(rf'{"|".join(dist_keys)}', text)
    dict_values = [i.strip() for i in parts]
    del dict_values[0]
    return dict(zip(dist_keys, dict_values))


# Определяем сколько слов будем печатать до и после искомого слова
def delta_index(index):
    if index < 5:
        return 0, index, index + 5
    else:
        return index - 5, index, index + 6


# Ищем слово и печатаем нужный отрезок
def find_the_word(word, dictionary, full=False):
    global count
    for item in dictionary.items():
        key = item[0]
        value = item[1]
        newlist = value.split(' ')
        if full:
            print(key)
            print(' '.join(newlist))
        else:
            try:
                index = newlist.index(word)
                finallist = ' '.join(newlist[(delta_index(index)[0]):(delta_index(index)[2])])
                print(key)
                print(f'{finallist[:finallist.index(word) - 1]} '
                      f'{Fore.RED}{word}{Style.RESET_ALL}'
                      f'{finallist[finallist.index(word) + len(word):150]}\n')
            except ValueError:
                pass
        count += 1


for file in list_of_log_files:
    print('Файл ' + Fore.GREEN + file)
    with open(os.path.join(logs_folder_path, file), 'r') as text_file:
        text = text_file.read()
    find_the_word(text_to_search, make_dict(text), args.full)

print('Поиск закончен')
print(f'Всего найдено совпадений: {count}')
