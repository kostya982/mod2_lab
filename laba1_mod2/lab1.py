from typing import List, Union


class MaterialObject:
    """
    Абстрактный класс, описывающий характеристики материальных объектов.

    Attributes:
        material (str): Материал, из которого сделан объект.
        weight (float): Вес объекта в кг.

    Methods:
        move(self, destination: str) -> None:
            Перемещает объект в указанное место.

        measure_weight(self) -> float:
            Измеряет вес объекта и возвращает его.

        break_down(self, parts: List[str]) -> None:
            Разбивает объект на указанные части.
    """

    def __init__(self, material: str, weight: float):
        """
        Конструктор класса MaterialObject.

        Args:
            material (str): Материал, из которого сделан объект.
            weight (float): Вес объекта в кг.
        """
        self.material = material
        self.weight = weight

    def move(self, destination: str) -> None:
        """
        Перемещает объект в указанное место.

        Args:
            destination (str): Место, куда нужно переместить объект.

        Example:
        >>> obj = MaterialObject("Wood", 10.5)
        >>> obj.move("Living Room")
        """
        pass

    def measure_weight(self) -> float:
        """
        Измеряет вес объекта и возвращает его.

        Returns:
            float: Вес объекта.

        Example:
        >>> obj = MaterialObject("Metal", 15.2)
        >>> obj.measure_weight()
        """
        pass

    def break_down(self, parts: List[str]) -> None:
        """
        Разбивает объект на указанные части.

        Args:
            parts (List[str]): Список частей, на которые нужно разбить объект.

        Example:
        >>> obj = MaterialObject("Glass", 5.0)
        >>> obj.break_down(["Top", "Bottom"])
        """
        pass


class LivingBeing:
    """
    Абстрактный класс, описывающий характеристики живых существ.

    Attributes:
        species (str): Вид живого существа.
        age (int): Возраст живого существа в годах.

    Methods:
        grow(self, years: int) -> None:
            Увеличивает возраст живого существа на указанное количество лет.

        reproduce(self) -> str:
            Запускает процесс размножения живого существа.

        communicate(self, message: str) -> str:
            Позволяет живому существу общаться с другими.
    """

    def __init__(self, species: str, age: int):
        """
        Конструктор класса LivingBeing.

        Args:
            species (str): Вид живого существа.
            age (int): Возраст живого существа в годах.
        """
        self.species = species
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст живого существа на указанное количество лет.

        Args:
            years (int): Количество лет, на которое увеличить возраст.

        Example:
        >>> being = LivingBeing("Human", 25)
        >>> being.grow(5)
        """
        pass

    def reproduce(self) -> str:
        """
        Запускает процесс размножения живого существа.

        Returns:
            str: Результат размножения.

        Example:
        >>> being = LivingBeing("Cat", 3)
        >>> being.reproduce()
        """
        pass

    def communicate(self, message: str) -> str:
        """
        Позволяет живому существу общаться с другими.

        Args:
            message (str): Сообщение для общения.

        Returns:
            str: Ответ на сообщение.

        Example:
        >>> being = LivingBeing("Dog", 7)
        >>> being.communicate("Woof!")
        """
        pass


class DigitalObject:
    """
    Абстрактный класс, описывающий характеристики цифровых (нематериальных) объектов.

    Attributes:
        name (str): Название цифрового объекта.
        data (Union[str, int, float]): Данные, связанные с цифровым объектом.
    """

    def __init__(self, name: str, data: Union[str, int, float]):
        """
        Конструктор класса DigitalObject.

        Args:
            name (str): Название цифрового объекта.
            data (Union[str, int, float]): Данные, связанные с цифровым объектом.
        """
        self.name = name
        self.data = data

    def process_data(self, algorithm: str) -> Union[str, int, float]:
        """
        Обрабатывает данные цифрового объекта в соответствии с заданным алгоритмом.

        Args:
            algorithm (str): Алгоритм обработки данных.

        Example:
        >>> obj = DigitalObject("Document", "A text document.", "Lorem ipsum")
        >>> obj.process_data("Compression")
        """
        pass