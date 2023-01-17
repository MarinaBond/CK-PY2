BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id_ < 0:
            raise ValueError("Идентификатор должен быть больше нуля")
        self.id_ = id_
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name
        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть больше нуля")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'

# TODO написать класс Library
class Library:
    def __int__(self, books: list[Book]):
        """
        :param books: Список книг
        :return:
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self, id_):
        if len(self.books) == 0:
            return 1
        else:
            return self.books.[-1].id_ + 1

    def get_index_by_book_id(self, id_):
        for ind, book in enumerate(self.books):
            if ind in book == id_:
                return ind
            else:
                raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id(1))  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id(1))  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
