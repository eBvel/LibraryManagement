def book_list_view(library):
    if library:
        print("\n-----СПИСОК КНИГ-----")
        for book in library.keys():
            print(f"Название: {book}")
    else:
        print("\nВ библиотеке отсутствуют книги!")


def main():
    library = {
        "Преступление и наказание": {'author': "Федор Достоевский",
                                     'publish_date': 1990,
                                     'is_available': False},
        "Идиот": {'author': "Федор Достоевский", 'publish_date': 1998,
                  'is_available': True},
        "Капитанская дочка": {'author': "Александр Пушкин",
                              'publish_date': 2001, 'is_available': False},
        "Вишневый сад": {'author': "Антон Чехов", 'publish_date': 1995,
                         'is_available': True},
        "Отцы и дети": {'author': "Иван Тургенев", 'publish_date': 2003,
                        'is_available': True}
    }

    book_list_view(library)


main()
