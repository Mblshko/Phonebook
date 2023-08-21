from utils import Phonebook
from file_menegement import File
from rich.console import Console
from rich.table import Table
from rich import box


console = Console()


class Interface:
    '''Класс интерфейса отвечает за вывод и ввод информаци от пользователя'''

    @staticmethod
    def start():
        '''Запускает программу и выводит главное меню'''

        while True:
            console.print("\nГЛАВНОЕ МЕНЮ:", style="bold blue")
            console.print("1. Показать все записи")
            console.print("2. Добавить новую запись")
            console.print("3. Редактировать запись")
            console.print("4. Удалить запись")
            console.print("5. Поиск")
            console.print("6. Выход")
            choice = console.input("Введите цифру: ",)

            if choice == "1":
                Interface.table_phonebook()
                console.input("Нажмите [bold green]Enter[/], чтобы продолжить")

            elif choice == "2":
                Phonebook.add_contact()
                console.print("\nЗапись успешно добавлена!", style="bold green")
                console.input("Нажмите [bold green]Enter[/], чтобы продолжить")

            elif choice == "3":
                console.print("\nЕсли что-то нужно оставить без изменений,"
                              " просто нажмите [bold green]Enter[/]", style="bold yellow")
                index = console.input("Введите номер [bold yellow]ID[/] контакта,"
                                      " который хотите изменить: ")
                if Phonebook.edit_contact(index):
                    console.print("\nЗапись успешно изменена", style="bold green")
                    console.input("Нажмите [bold green]Enter[/], чтобы продолжить")
                else:
                    console.print("\nВы неправильно ввели номер [bold yellow]ID[/]",
                                  style="bold red")
                    console.input("Нажмите [bold green]Enter[/], чтобы продолжить")

            elif choice == "4":
                index = console.input("\nВведите номер [bold yellow]ID[/] контакта, который хотите удалить: ")
                if Phonebook.delete_contact(index):
                    console.print("\nКонтакт удалён", style="bold green")
                else:
                    console.print("\nВы неправильно ввели номер [bold yellow]ID[/]",
                                  style="bold red")
                console.input("Нажмите [bold green]Enter[/], чтобы продолжить")

            elif choice == "5":
                search = console.input("Введите через пробел данные для поиска: ")
                result = Phonebook.search_contact(search)
                if result:
                    Interface.table_phonebook(result)
                else:
                    console.print("\nНичего не найдено", style="bold yellow")
                console.input("Нажмите [bold green]Enter[/], чтобы продолжить")

            elif choice == "6":
                break

            else:
                console.print("Пожалуйста вводите только [bold yellow]цифру[/]"
                              " из списка меню!", style="bold")

    @staticmethod
    def table_phonebook(search=None):
        '''Вывод данные файла в удобную таблицу'''

        table = Table(title="Телефонный справочник", box=box.HEAVY)
        data = File.file_read()
        for i, column in enumerate(data[0]):
            table.add_column(column, justify="center")
        if search:
            for row in search:
                table.add_row(*row)
        else:
            if data[1:]:
                for row in data[1:]:
                    table.add_row(*row)
        console.print(table)
