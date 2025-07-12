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


def main():
    book_list_view()


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
main()
