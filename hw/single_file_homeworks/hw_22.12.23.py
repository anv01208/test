# 1

input = input("Введите слово для проверки: ")

result = list(input)
res = False

for i in result:
    a = 0
    b = -1
    if result[a] == result[b]:
        res = True
        a += 1
        b -= 1
    else:
        break

if res != False:
    print("Слово палидром!")
else:
    print("Слово НЕ палидром!")

# 2

input = input("Введите слово: ")

result = list(input)

if len(result) >= 3:
    a = result[-3]
    b = result[-2]
    c = result[-1]
    print(f"Последние 3 символа: {a}{b}{c}")
else:
    print("Слишком короткое слово!")


















