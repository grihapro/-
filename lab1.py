# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Box:
    def __init__(self, capacity: float, fragile: bool, empty_space: float):
        """
        Создание и подготовка к работе объекта "Коробка"

        :param capacity: Объем коробки
        :param fragile: Хрупкость содержимого
        :param empty_space: Свободное место

        Примеры:
        >>> box = Box(1000, True, 100) #инициализация экземпляра класса
        """
        if not isinstance(capacity, (float, int)):
            raise TypeError("Объём коробки должен быть типа float или int")
        if capacity <= 0:
            raise ValueError("Объём коробки не может быть меньше либо равен 0")
        self.capacity = capacity

        if not isinstance(fragile, bool):
            raise TypeError("Хрупкость содержимого коробки должны быть типа bool")
        self.fragile = fragile

        if not isinstance(empty_space, (float, int)):
            raise TypeError("Свободное место коробки должно быть типа float или int")
        if empty_space < 0:
            raise ValueError("Свободное место не может быть отрицательным числом")
        self.empty_space =empty_space

    def check(self) -> bool:
        """
        Функция проверяет является ли содержимое коробки хрупким объектом

        :return: Является ли содержимое хрупким

        Примеры:
        >>> box = Box(1000, False, 300)
        >>> box.check()
        """
        ...

    def replace_object(self, fragile: bool, capacity_object: float) -> None:
        """
        Функция меняет объект в коробкe

        :param fragile: Хрупкость нового объекта
        :param capacity_object: Объем нового объекта

        :raise ValueError: Если объем нового объекта больше объема коробки, то вызываем ошибку

        Примеры:
        >>> box = Box(1000, True, 500)
        >>> box.replace_object(False, 400)
        """
        if not isinstance(fragile, bool):
            raise TypeError("Хрупкость содержимого коробки должны быть типа bool")

        if not isinstance(capacity_object, (float, int)):
            raise TypeError("Объем объекта должен быть типа float или int")
        if capacity_object <= 0 or capacity_object > self.capacity:
            raise ValueError("Объем объекта должен быть положительным числом, не превышающим размера коробки")
        ...


class Glasses:
    def __init__(self, cost: float, sunglasses: bool, purity: bool):
        """
        Создание и подготовка к работе объекта "Очки"

        :param cost: Стоимость очков
        :param sunglasses: Являются ли очки солнезащитными
        :param purity: Чистота очков

        Примеры:
        >>> glasses = Glasses(1500, False, True)
        """
        if not isinstance(cost, (float, int)):
            raise TypeError("Стоимость очков должна быть типа float или int")
        if cost < 0:
            raise ValueError("Стоимость очков не может быть меньше нуля")
        self.cost = cost

        if not isinstance(sunglasses, bool):
            raise TypeError("Параметр, определяющий солнцезащитные ли очки должен быть типа bool")
        self.sunglasses = sunglasses

        if not isinstance(purity, bool):
            raise TypeError("Чистота очков должна быть типа bool")
        self.purity = purity

    def sun_protection(self) -> bool:
        """
        Функция, которая проверяет солнезащитные очки или нет

        :return: Являются ли очки солнцезащитными

        Примеры:
        >>> glasses = Glasses(2000, True, True)
        >>> glasses.sun_protection()
        """
        ...

    def clean(self) -> bool:
        """
        Чистка очков, если она необохима.

        :return: Возвращает True, если чистка была или False, если нет

        Примеры:
        >>> glasses = Glasses(2000, True, False)
        >>> glasses.clean()
        """
        ...


class Watermelon:
    def __init__(self, weight: float, seeds: int, ripeness: bool):
        """
        Создание и подготовка к работе объекта "Арбуз"

        :param weight: Вес арбуза
        :param seeds: Количество семян арбуза
        :param ripeness: Спелость арбуза

        Примеры:
        >>> melon = Watermelon(5, 100, True)
        """
        if not isinstance(weight, (float, int)):
            raise TypeError("Вес арбуза должен быть типа float или int")
        if weight <= 0:
            raise ValueError("Вес арбуза не может быть меньше или равно 0")
        self.weight = weight

        if not isinstance(seeds, int):
            raise TypeError("Количество семян арбуза должно быть типа int")
        if seeds < 0:
            raise ValueError("Количество семян не может быть меньше 0")
        self.seeds = seeds

        if not isinstance(ripeness, bool):
            raise TypeError("Спелость арбуза должна быть типа bool")
        self.ripeness = ripeness

    def knock(self) -> bool:
        """
        Функция, которая проверяет спелый ли арбуз.

        :return: Спелость арбуза

        Примеры:
        >>> melon = Watermelon(5, 100, False)
        >>> melon.knock()
        """
        ...

    def clear(self) -> None:
        """
        Отчистка арбуза от семян.

        Примеры:
        >>> melon = Watermelon(5, 100, True)
        >>> melon.clear()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
