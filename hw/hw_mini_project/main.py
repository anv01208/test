# Alt + Enter
from books import Book
from libraries import Library
from users import User

library = Library()

book1 = Book('Гарри Поттер', 'Дж.К. Роулинг', 'Фэнтэзи')
book2 = Book('1984', 'Оруэлл', 'Антиутопия')
book3 = Book('Оно', 'Стивен Кинг', 'Ужасы')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

maxim = User('Max')

print("В библиотеке:", library.get_available_books())
print("У Максима:", maxim.get_books())

print("\nМаксим берет книгу из библиотеки...\n")
maxim.take_book(book1)

print("В библиотеке:", library.get_available_books())
print("У Максима:", maxim.get_books())

print("\nМаксим возвращает книгу в библиотеку...\n")
maxim.return_book(book1)

print("В библиотеке:", library.get_available_books())
print("У Максима:", maxim.get_books())

print("\nПоиск книг по жанру - 'Ужасы'...")  # поиск по жанру
print(f'Ужасы: {library.search_by_genre("Ужасы")}')
print()
