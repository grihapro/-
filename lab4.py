import doctest


class Pet:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Питомец"

        :param name: Имя питомца
        :param age: Возраст питомца

        Примеры:
        >>> pet = Pet("Шарик", 2) #инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя питомца должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise ValueError("Возраст питомца должен быть типа int")
        if age < 0:
            raise TypeError("Возраст питомца не может быть меньше нуля")
        self.age = age

    def feed(self, food: str) -> None:
        """
        Функция кормежки питомца

        :param food: Еда, которой будете кормить питомца

        Примеры:
        >>> pet = Pet("Шарик", 2)
        >>> pet.feed("Мясо")
        """
        if not isinstance(food, str):
            raise TypeError("Название еды должно быть типа str")
        ...

    def play(self) -> None:
        """
        Функция игры с питомцем

        Примеры:
        >>> pet = Pet("Шарик", 2)
        >>> pet.play()
        """
        ...

    def __repr__(self):
        """
        Фукнция __repr__ для класса Питомец
        """
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"

    def __str__(self):
        """
        Фукнция __str__ для класса Питомец
        """
        return f"Питомец {self.name}. Возраст {self.age}"


class Dog(Pet):
    def __init__(self, name: str, age: int, angry: bool):
        """
        Создание и подготовка к работе объекта "Собака"

        :param name: Имя собаки
        :param age: Возраст собаки
        :param angry: Агрессивная ли собак

        Примеры:
        >>> dog = Dog("Шарик", 2, False) #инициализация экземпляра класса
        """
        super().__init__(name, age)
        if not isinstance(angry, bool):
            raise TypeError("Агрессивность собаки должна быть типа bool")
        self.angry = angry

    def feed(self, food: str) -> None:
        """
        Функция кормежки собаки (унаследование метода базового класса)

        :param food: Еда, которой будете кормить собаку

        Примеры:
        >>> dog = Dog("Шарик", 2, False)
        >>> dog.feed("Мясо")
        """
        super().feed(food)
        ...

    def play(self) -> bool:
        """
        Функция игры с питомцем (перегрузка метода базового класса)

        :return: Возвращает True, если собака не агрессивная, или False, если агрессивная

        Примеры:
        >>> dog = Dog("Шарик", 2, False)
        >>> dog.play()
        """
        ...

    def __repr__(self):
        """
        Фукнция __repr__ для класса Собака
        """
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age}, angry={self.angry})"

    def __str__(self):
        """
        Фукнция __str__ для класса Собака
        """
        return super().__str__() + f". Агрессивная {self.angry}"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
