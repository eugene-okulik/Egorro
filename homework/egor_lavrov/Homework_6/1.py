'''Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
После этого выводит получившийся текст на экран.
Знаки препинания не должны оказаться внутри слова.
Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
но уже преобразованного.'''

text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

new_text = []

for word in text.split(' '):
    if word.endswith(',') or word.endswith('.'):
        new_text.append(word[:-1] + 'ing' + word[-1])
    else:
        new_text.append(word + 'ing')

print(' '.join(new_text))
