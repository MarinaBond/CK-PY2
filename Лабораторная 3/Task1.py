class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        Дочерний класс 'Бумажная книга'
        :param name: Название книги
        :param author: Автор
        :param pages: Количество страниц
        """
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц книги должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        super_ = super().__repr__()
        return f"{super_}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        Дочерний класс 'Аудиокнига'
        :param name: Название книги
        :param author: Автор
        :param duration: Продолжительность
        """
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть больше нуля")
        self.duration = duration

    def __repr__(self):
        super_r = super().__repr__()
        return f"{super_r}"

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"


if __name__ == "__main__":
    book_1 = PaperBook('Гарри Поттер и узник Азкабана', 'Роулинг Джоан Кэтлин', 328)
    book_2 = AudioBook('Печальный кипарис', 'Агата Кристи', 7.16)
    print(book_1)
    print(book_2)