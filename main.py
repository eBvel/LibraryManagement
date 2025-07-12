import datetime


def request_menu_item(menu_operations):
    try:
        menu_item = int(input("\nВведите пункт меню: "))
        menu_operations[menu_item]()
    except ValueError:
        print("Ошибка: введено некорректное значение!")
    except KeyError:
        print("Ошибка: указанный пункт меню отсутствует!")


def request_book_title():
    while True:
        try:
            title = input("Введите название книги: ")
            return title
        except ValueError:
            print("Ошибка: поле не заполнено!")


def request_author_name():
    while True:
        try:
            name = input("Введите имя и фамилию автора (через пробел): ")
            is_error = validate_author(" ".join(name.split()))
            if is_error:
                print(is_error)
            else:
                return name
        except ValueError:
            print("Ошибка: поле не заполнено!")


def request_publish_date():
    while True:
        try:
            year = int(input("Введите дату публикации: "))
            if year < 1800 or year > datetime.date.today().year:
                print("Ошибка: введено значение за пределами установленного "
                      "диапазона!")
            else:
                return year
        except ValueError:
            print("Ошибка: введено нечисловое значение!")


def validate_author(name):
    if len(name) < 6 or len(name) > 30:
        return ("Ошибка: длина введенного значения не соответствует "
                "установленному диапазон!")

    allowed_characters = set("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' абвгдеёжзий"
                             "клмнопрстуфхцчшщъыьэюя")
    for letter in name:
        if letter not in allowed_characters:
            return "Ошибка: введено недопустимое значение!"
    return ""


def book_list_view():
    if library:
        print("\n-----СПИСОК КНИГ-----")
        for book in library.keys():
            print(f"Название: {book}")
    else:
        print("\nВ библиотеке отсутствуют книги!")


def add_book(title, author, year):
    def perform_addition(text):
        new_book = {title: {author_key: author, year_key: year,
                            available_key: None}}
        library.update(new_book)
        print(text)

    if title in library:
        answer = to_ask(f"Книга '{title}' уже есть в библиотеке.\nЖелаете "
                        f"обновить данные?")
        if answer:
            perform_addition(f"Данные книги '{title}' - обновлены!")
        else:
            print("Обновление отменено!")
    else:
        perform_addition(f"Книга '{title}' - добавлена в библиотеку!")


def to_ask(question):
    answers = {'да': True, 'нет': False}
    while True:
        try:
            answer = input(f"{question} (да/нет): ").lower()
            return answers[answer]
        except KeyError:
            print("Ошибка: введен некорректный ответ!")


def add_book_to_library():
    title = request_book_title()
    author = request_author_name()
    year = request_publish_date()
    add_book(title, author, year)


def complete_program():
    global at_work
    at_work = False
    print("Программа завершена!")


def start_menu():
    print("""
-------БИБЛИОТЕКА-------
 МЕНЮ:
 1. Вывести список книг;
 2. Добавить книгу;
 3. Выход.""")


def main():
    while at_work:
        menu_operations = {1: book_list_view, 2: add_book_to_library, 3: complete_program}
        request_menu_item(menu_operations)


author_key = 'author'
year_key = 'publish_date'
available_key = 'is_available'
library = {
    "Преступление и наказание": {author_key: "Федор Достоевский",
                                 year_key: 1990,
                                 available_key: False},
    "Идиот": {author_key: "Федор Достоевский", year_key: 1998,
              available_key: True},
    "Капитанская дочка": {author_key: "Александр Пушкин",
                          year_key: 2001, available_key: False},
    "Вишневый сад": {author_key: "Антон Чехов", year_key: 1995,
                     available_key: True},
    "Отцы и дети": {author_key: "Иван Тургенев", year_key: 2003,
                    available_key: True}
}
at_work = True
start_menu()
main()
