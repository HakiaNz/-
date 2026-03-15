
class Car:
    """
    Базовый класс, представляющий автомобиль.

    Атрибуты:
        make (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска.
        color (str): Цвет кузова.
        _vin (str): Идентификационный номер (VIN), защищённый атрибут.
        __engine_number (str): Номер двигателя, приватный атрибут.
    """

    def __init__(self, make: str, model: str, year: int, color: str, vin: str, engine_number: str) -> None:
        """
        Инициализирует экземпляр класса Car.

        :param make: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param color: Цвет кузова.
        :param vin: VIN-номер.
        :param engine_number: Номер двигателя.
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self._vin = vin
        self.__engine_number = engine_number

    def __str__(self) -> str:
        """
        Возвращает удобочитаемое строковое представление автомобиля.

        :return: Строка с описанием автомобиля.
        """
        return f"{self.color} {self.make} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает строку, которая может быть использована для воссоздания объекта.
        Включает все основные атрибуты, включая защищённые и приватные (для отладки).

        :return: Строка с детальным представлением.
        """
        return (f"Car(make={self.make!r}, model={self.model!r}, year={self.year!r}, "
                f"color={self.color!r}, vin={self._vin!r}, engine_number={self.__engine_number!r})")

    def start_engine(self) -> None:
        """
        Запускает двигатель. Выводит сообщение в консоль.
        """
        print("Engine started.")

    def get_info(self) -> str:
        """
        Возвращает основную информацию об автомобиле.

        :return: Строка с основными характеристиками.
        """
        return f"{self.make} {self.model}, {self.year} year, {self.color}"


class PassengerCar(Car):
    """
    Дочерний класс, представляющий легковой автомобиль.
    Расширяет базовый класс Car атрибутами, специфичными для легковых авто.

    Атрибуты:
        body_style (str): Тип кузова (седан, хэтчбек, универсал и т.д.).
        doors (int): Количество дверей.
    """

    def __init__(self, make: str, model: str, year: int, color: str, vin: str, engine_number: str,
                 body_style: str, doors: int) -> None:
        """
        Инициализирует экземпляр класса PassengerCar.
        Расширяет конструктор базового класса.

        :param make: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param color: Цвет кузова.
        :param vin: VIN-номер.
        :param engine_number: Номер двигателя.
        :param body_style: Тип кузова.
        :param doors: Количество дверей.
        """
        super().__init__(make, model, year, color, vin, engine_number)
        self.body_style = body_style
        self.doors = doors

    def __str__(self) -> str:
        """
        Переопределённый метод. Возвращает строковое представление легкового автомобиля,
        добавляя информацию о типе кузова и дверях.

        :return: Строка с описанием легкового автомобиля.
        """
        base_str = super().__str__()
        return f"{base_str}, {self.body_style}, {self.doors} doors"

    def __repr__(self) -> str:
        """
        Переопределённый метод. Возвращает детальное представление с учётом новых атрибутов.

        :return: Строка для отладки.
        """
        base_repr = super().__repr__()
        base_repr = base_repr.rstrip(')')
        return f"{base_repr}, body_style={self.body_style!r}, doors={self.doors!r})"

    def get_info(self) -> str:
        """
        Перегружает метод базового класса. Возвращает расширенную информацию,
        включая тип кузова и количество дверей.

        :return: Строка с информацией о легковом автомобиле.
        """
        base_info = super().get_info()
        return f"{base_info}, body: {self.body_style}, doors: {self.doors}"


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, "silver", "JTDBE32K123456789", "2GR-FE123456")
    print("Базовый автомобиль:")
    print(str(car))
    print(repr(car))
    car.start_engine()
    print(car.get_info())
    print()

    passenger = PassengerCar("Honda", "Civic", 2021, "red", "2HGFA1F53PH123456", "K20C2123456",
                             "sedan", 4)
    print("Легковой автомобиль:")
    print(str(passenger))
    print(repr(passenger))
    passenger.start_engine()
    print(passenger.get_info())