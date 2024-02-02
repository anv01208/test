input = int(input("Введите цифру: "))
result = 1

for i in range(1, input + 1):
    result = result * i
print(f"{i}! = {result}\n")
