from books import Book
from libraries import Library
from users import User


def get_library_with_books():
    library = Library()

    book1 = Book('Гарри Поттер', 'Дж.К. Роулинг', 'Фэнтэзи')
    book2 = Book('1984', 'Оруэлл', 'Антиутопия')
    book3 = Book('Оно', 'Стивен Кинг', 'Ужасы')

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    return library
