
class Wall:
    def __init__(self, height: int, width: int):
        """
        Создание и подготовка объекта "Стена"
        :param height: Высота стены
        :param width: Ширина стены

        Пример:
        >>> wall = Wall(4, 10)
        """
        if not isinstance(height, int):
            raise TypeError("Высота стены должна быть типа int")
        if height <= 0:
            raise ValueError("Высота стены должна быть больше нуля")
        self.height = height

        if not isinstance(width, int):
            raise TypeError("Ширина стены должна быть типа int")
        if width <= 0:
            raise ValueError("Ширина стены должна быть больше нуля")
        self.width = width

    def make_the_wall_higher(self, meters: (int, float)) -> None:
        """
        Увеличение стены
        :param meters: Количество метров, на которое увеличивается стена

        Пример:
        >>> wall1 = Wall(3, 8)
        >>> wall1.make_the_wall_higher(2)
        """
        ...

    def destroy_the_wall(self, break_meters: (int, float)) -> None:
        """
        Разрушение стены
        :param break_meters: Количество метров на которое сносим стену
        :raise ValueError: Если количество метров на которое уменьшается стена, превышает высоту стены, вызываем ошибку

        :return: Количество метров, на которое уменьшили стену

        Пример:
        >>> wall2 = Wall(3, 5)
        >>> wall2.destroy_the_wall(1)
        """
        ...


class Telegram:
    def __init__(self, viewed_posts: int, number_of_notifications: int) -> None:
        """
        Создание и подготовка объекта "Телеграм"
        :param viewed_posts: Просмотренные посты
        :param number_of_notifications: Количество уведомлений

        Пример:
        >>> telegram = Telegram(10, 3)
        """
        if not isinstance(viewed_posts, int):
            raise TypeError("Просмотренные посты должны быть типа int")
        if viewed_posts < 0:
            raise ValueError("Количество постов не должно быть отрицательным")
        self.viewed_posts = viewed_posts

        if not isinstance(number_of_notifications, int):
            raise TypeError("Количество уведомлений должно быть типа int")
        if number_of_notifications < 0:
            raise ValueError("Количество уведомлений не должно быть отрицательным")
        self.number_of_notifications = number_of_notifications

    def new_notification(self,) -> bool:
        """
        Метод, который проверяет есть ли новые уведомления

        :return: Есть ли новые уведомления

        Пример:
        >>> telegram = Telegram(10,5)
        >>> telegram.new_notification()
        """
        ...

    def read_posts(self, viewed_posts: int) -> None:
        """
        Метод, который увеличивает количество просмотренных постов
        :param viewed_posts: Количество просмотренных постов

        Пример:
        >>> telegram = Telegram(12, 4)
        >>> telegram.read_posts(20)
        """
        ...


class Window:
    def __init__(self, name: str, number: int) -> None:
        """
        Создание и подготовка объекта "Окно"
        :param name: Название окна
        :param number: Количество окон

        Пример:
        >>> window = Window('Google Chrome', 3)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа int")
        self.name = name

        if not isinstance(number, int):
            raise TypeError("Количество окон должно быть типа int")
        if number < 0:
            raise ValueError("Количество окон должно быть положительным числом")
        self.number = number

    def count_windows(self, new_window: int) -> None:
        """
        Метод считает количество новых открытых окон
        :param new_window: Количество новых окон

        Пример:
        >>> window = Window('Яндекс Браузер', 15)
        >>> window.count_windows(10)
        """
        if not isinstance(new_window, int):
            raise TypeError("Количество окон должно быть типа int")
        if new_window < 0:
            raise ValueError("Количество окон должно быть положительным числом")
        ...

    def open_win(self) -> bool:
        """
        Метод определяет есть ли открытые окна
        :return: Есть ли открытые окна

        Пример:
        >>> window = Window('Music', 1)
        >>> window.open_win()
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
