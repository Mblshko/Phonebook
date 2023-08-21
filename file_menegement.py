import csv


class File:
    '''Работа с файлом'''

    @staticmethod
    def file_create():
        '''Создаёт файл и добавляет первую строчку название колонок'''
        with open("telephone_book.csv", "w", encoding="utf-8", newline='') as book:
            book.write(f"ID,Фамилия,Имя,Отчество,Название организации,"
                       f"Рабочий телефон,Личный телефон\n")

    @staticmethod
    def file_read():
        '''Читает данные с файла и передаёт их двухмерным списком'''
        data = []
        with open("telephone_book.csv", "r", encoding="utf-8") as book:
            reader = csv.reader(book)
            for line in reader:
                data.append(line)
        return data

    @staticmethod
    def file_append(data):
        '''Добавляет в конец файла новую запись'''
        with open("telephone_book.csv", "a", encoding="utf-8", newline='') as book:
            writer = csv.writer(book)
            writer.writerow(data)

    @staticmethod
    def file_write(data):
        '''Перезаписывает весь файл. Используется для удаления и редактирования'''
        with open("telephone_book.csv", "w", encoding="utf-8", newline='') as book:
            writer = csv.writer(book)
            writer.writerows(data)
