from file_menegement import File
from text_processing import Processing


class Phonebook:
    '''Данный класс содержит функционал CRUD'''

    @staticmethod
    def add_contact():
        '''Читаем информацию, преобразуем и добавляем в телефонную книгу'''

        messages = ["Введите фамилию: ", "Введите имя: ", "Введите отчество: ",
                    "Введите название организации: ", "Введите рабочий номер телефона: ",
                    "Введите личный номер телефона: "]

        data = [Processing.get_pk()]
        for i, mes in enumerate(messages):
            info = input(mes).strip()
            if info:
                if i <= 3:
                    info = Processing.firstchar_upper(info)
            else:
                info = "-"
            data.append(info)
        File.file_append(data)

    @staticmethod
    def edit_contact(index):
        '''Редактирует контакт выбранный по ID'''

        index = Processing.index_valid(index)
        data = File.file_read()
        edit_data = []
        if 0 < index <= (len(data) - 1):
            edit_data.append(data[index][0])
            for i, item in enumerate(data[index][1:], 1):
                info = input(f"{data[0][i]}: {item} - изменить на: ")
                if not info:
                    edit_data.append(data[index][i])
                    continue
                if i <= 4:
                    info = Processing.firstchar_upper(info)
                edit_data.append(info)
            del data[index]
            data.insert(index, edit_data)
            File.file_write(data)
            return True
        else:
            return False

    @staticmethod
    def delete_contact(index):
        '''Удаляет запись согласно ID введённого пользователем'''

        index = Processing.index_valid(index)
        data = File.file_read()
        if 0 < index <= (len(data) - 1):
            del data[index]
            File.file_write(data)
            Processing.set_pk()
            return True
        else:
            return False

    @staticmethod
    def search_contact(search):
        '''Поиск контактов с одной или несколькими характеристиками'''

        search_split = [Processing.firstchar_upper(text) for text in search.split()]
        data = File.file_read()
        stack = None
        result = []
        for line in data:
            for item in search_split:
                if item in line:
                    stack = line
                else:
                    stack = None
            if stack:
                result.append(stack)
            stack = None

        if not result:
            return False
        return result
