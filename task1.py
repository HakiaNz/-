class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"{self.__class__.__name__}: '{self._name}' | {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self._name}', author='{self._author}')"
class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages 
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга: '{self._name}' | Автор: {self._author} | Страниц: {self._pages}"
class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")
        self._duration = float(value)

    def __str__(self):
        return f"Аудиокнига: '{self._name}' | Автор: {self._author} | Длительность: {self._duration} ч."
