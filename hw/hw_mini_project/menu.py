from users import User
from data import get_library_with_books

library = get_library_with_books()

maxim = User('Max')

print(f"Добро пожаловать в нашу Библиотеку!\n")
user_input = None

while user_input != 'q':
    print("Меню:\n"
          "1. Все доступные книги\n"
          "2. Взять книгу\n"
          "3. Посмотреть взятые книги\n"
          "4. Вернуть книгу\n\n")

    user_input = input("Выберите из меню [1-4] ('q' - выйти): ")

    if user_input == '1':
        print(library.get_available_books())

    elif user_input == '2':
        books = library.get_available_books()
        for i in range(len(books)):
            print(f"{i}. {books[i]}")

        ind = int(input("Выберите книгу: "))

        maxim.take_book(books[ind])
        print("Приятного чтения!\n\n")

    elif user_input == '3':
        print("Ваши взятые книги:")
        taken_books = maxim.get_books()
        for i in range(len(taken_books)):
            print(f"{i}. {taken_books[i]}")

    elif user_input == '4':
        print("Ваши взятые книги:")
        taken_books = maxim.get_books()
        for i in range(len(taken_books)):
            print(f"{i}. {taken_books[i]}")

        ind = int(input("Выберите книгу для возврата: "))
        maxim.return_book(maxim.get_books()[ind])
        print("Книга успешно возвращена!\n\n")
    elif user_input == 'q':
        print("До свидание!")
    else:
        print("Не правильная опция, прошу выбрать из меню!\n\n")
