class Book:

    def __init__(self, title, author, number_of_pages, page_material, ISBN, presence_of_text, reserved):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.page_material = page_material
        self.ISBN = ISBN
        self.presence_of_text = presence_of_text
        self.reserved = reserved

    def info(self):
        print(f'Название: {self.title}\n'
              f'Автор: {self.author}\n'
              f'Страниц: {self.number_of_pages}\n'
              f'Материал страниц: {self.page_material}\n'
              f'ISBN: {self.ISBN}')
        if self.reserved:
            print(f'Зарезервирована\n')
        else:
            print('')  # Для отделения информации между книгами


class SchoolBook(Book):

    def __init__(self, title, author, number_of_pages, page_material, ISBN, presence_of_text, reserved,
            subject, grade, presence_of_assignment):
        super().__init__(title, author, number_of_pages, page_material, ISBN, presence_of_text, reserved)
        self.subject = subject
        self.grade = grade
        self.presence_of_assignment = presence_of_assignment

    def info(self):
        print(f'Название: {self.title}\n'
              f'Автор: {self.author}\n'
              f'Страниц: {self.number_of_pages}\n'
              f'Предмет: {self.subject}\n'
              f'Класс: {self.grade}')
        if self.reserved:
            print('Зарезервирована\n')
        else:
            print('')  # Для отделения информации между книгами


DFM_01 = Book('Идиот', 'Достоевский Фёдор Михайлович', '640',
              'Офсетная бумага', '978-5-04-154195-8', True, True)
DFM_02 = Book('Униженные и оскорблённые', 'Достоевский Фёдор Михайлович', '448',
              'Офсетная бумага', '978-5-17-135181-6', True, False)
PAS_01 = Book('Стихотворения. Поэмы', 'Пушкин Александр Сергеевич', '512',
              'Офсетная бумага', '978-5-04-102518-2', True, True)
dSEA_01 = Book('Маленький принц и Цитадель', 'де Сент-Экзюпери Антуан', '488',
              'Офсетная бумага', '978-5-04-173229-5', True, False)
BIG_01 = Book('Что? Зачем? Почему?', 'Барановская Ирина Геннадьевна', '256',
              'Мелованная бумага', '978-5-17-094259-6', True, False)

sb_NSM_05 = SchoolBook('Математика. 5 класс', 'Никольский Сергей Михайлович', '272',
                       'Офсетная бумага', '978-5-09-018849-4', True, True,
                       'Математика', 5, True)
sb_CGI_10 = SchoolBook('Логика', 'Челпанов Георгий Иванович', '256',
                       'Офсетная бумага', '978-5-04-208121-7', True, True,
                       'Логика', 10, True)
sb_BNS_11 = SchoolBook('История России. С древнейших времён до 1914 г.', 'Борисов Николай Сергеевич', '384',
                       'Офсетная бумага', '978-5-09-113475-9', True, False,
                       'История', 11, False)


DFM_01.info()
DFM_02.info()
PAS_01.info()
dSEA_01.info()
BIG_01.info()

sb_NSM_05.info()
sb_CGI_10.info()
sb_BNS_11.info()
