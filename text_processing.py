from file_menegement import File


class Processing:
    '''Обработка и преобразование данных'''

    @staticmethod
    def get_pk():
        '''Возвращает новый ID согласно последней записи'''
        data = File.file_read()
        if len(data) == 1:
            return 1
        return int(data[-1][0]) + 1

    @staticmethod
    def firstchar_upper(string):
        '''Делаем первую букву заглавной в ФИО и названии организации'''
        firstchar = string[0].upper()
        return firstchar + string[1:]

    @staticmethod
    def set_pk():
        '''Пересчитывает ID после удаления'''
        data = File.file_read()
        new_data = []
        for i, line in enumerate(data, 0):
            if i > 0:
                line[0] = i
            new_data.append(line)
        File.file_write(new_data)

    @staticmethod
    def index_valid(index):
        '''Проверяет правильно ли пользователь ввёл индекс'''
        if index.isdigit():
            return int(index)
        else:
            print(f"Ошибка! '{index}' не является числом!")
            return False
