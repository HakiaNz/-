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
class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:

        return f'Книга "{self.name}"'

    def __repr__(self) -> str:

        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books: list = None):
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index

        raise ValueError(f"Книги с id={book_id} нет в библиотеке")

if __name__ == "__main__":
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())
    print(library_with_books.get_index_by_book_id(1))


