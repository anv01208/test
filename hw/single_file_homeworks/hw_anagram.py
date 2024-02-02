def anagram(*args):
    list_1 = list(input_1)
    list_2 = list(input_2)

    list_1.sort()
    list_2.sort()

    if list_1 == list_2:
        print("Слова являются анаграммами!")
    else:
        print("Слова НЕ являются анаграммами!")


print("-------------------------")
print("< Проверка на анаграмму >")
print("-------------------------")

input_1 = input("Первое слово: ")
input_2 = input("Второе слово: ")

anagram(input_1, input_2)
