class Flower:

    def __init__(self, name, color, freshness, stem_length, cost):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_lenght = stem_length
        self.cost = cost


class Bouquet(Flower):

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def price(self):
        price = 0
        for flower in self.content:
            price += flower.cost
        return price

    def life_time(self):
        sum_times = 0
        for flower in self.content:
            sum_times += flower.freshness
        return sum_times//len(self.content)

    def sort_by(self, attr):
        print(f'\nБукет "{self.name}", сортировка по {attr}:')
        dictionary = {}
        for flower in self.content:
            dictionary[flower.name] = getattr(flower, attr)
        sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))
        for item in sorted_dictionary.items():
            print(*item, sep=': ')

    def find_by(self, attr, value):
        print(f'\nБукет "{self.name}", цветы с {attr} {value}:')
        dictionary = {}
        for flower in self.content:
            dictionary[flower.name] = getattr(flower, attr)
        filtered_dictionary = {key: val for key, val in dictionary.items() if val == value}
        if len(filtered_dictionary) != 0:
            for item in filtered_dictionary.items():
                print(*item, sep=': ')
        else:
                print('Таких цветов нет.')

class Rose(Flower):

    def __init__(self, name, color, freshness, stem_length, cost):
        super().__init__(name, color, freshness, stem_length, cost)


class Lilium(Flower):

    def __init__(self, name, color, freshness, stem_length, cost):
        super().__init__(name, color, freshness, stem_length, cost)


class Alstroemeria(Flower):
    def __init__(self, name, color, freshness, stem_length, cost):
        super().__init__(name, color, freshness, stem_length, cost)


class Eustoma(Flower):
    def __init__(self, name, color, freshness, stem_length, cost):
        super().__init__(name, color, freshness, stem_length, cost)


class Chrysanthemum(Flower):
    def __init__(self, name, color, freshness, stem_length, cost):
        super().__init__(name, color, freshness, stem_length, cost)


class LimoniumSinuatum(Flower):
    def __init__(self, name, color, freshness, stem_length, cost):
        super().__init__(name, color, freshness, stem_length, cost)


Rose_Candlelight_Cr = Rose('Роза Канделайт',
                           'Кремовый',5,60,500)
Lilium_Candidum = Lilium('Лилиля Белоснежная',
                         'Белый', 7, 80, 750)
Alstroemeria_Pelegrina = Alstroemeria('Альстромерия Пелегрина',
                                      'Розовый', 12, 70, 250)
Eustoma_Super_magic_Lilac = Eustoma('Эустома Супер Маджик',
                                    'Лиловый', 9, 70, 600)
Chrysanthemum_Carinatum = Chrysanthemum('Хризантема Ладьевидная',
                                        'Желтый', 15, 60, 300)
LimoniumSinuatum_Bl = LimoniumSinuatum('Статица',
                                       'Синий', 20, 60, 450)

Bouquet_Gentle_spring = Bouquet('Нежная весна',
                                [Alstroemeria_Pelegrina,
                                        Eustoma_Super_magic_Lilac,
                                        Lilium_Candidum])
Bouquet_Impression = Bouquet('Впечатление',
                             [Rose_Candlelight_Cr,
                                     Alstroemeria_Pelegrina,
                                     Eustoma_Super_magic_Lilac])
Bouquet_Сourage = Bouquet('Смелость',
                          [Rose_Candlelight_Cr,
                                  Chrysanthemum_Carinatum,
                                  LimoniumSinuatum_Bl])

print(f'Букет "{Bouquet_Impression.name}" стоит {Bouquet_Impression.price()} руб.')
print(f'Букет "{Bouquet_Impression.name}" сможет простоять около {Bouquet_Impression.life_time()} дней')

Bouquet_Impression.sort_by('cost')
Bouquet_Impression.sort_by('color')
Bouquet_Сourage.sort_by('freshness')
Bouquet_Gentle_spring.sort_by('stem_lenght')

Bouquet_Impression.find_by('color', 'Кремовый')
Bouquet_Gentle_spring.find_by('stem_lenght', 70)
Bouquet_Сourage.find_by('freshness', 10)
