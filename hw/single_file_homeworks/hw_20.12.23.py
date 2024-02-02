# 1
print("1 exercise:")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in list:
    if i % 2 == 0:
        sum = sum + i

print(f"Sum of even numbers: {sum}", end="\n\n")  # \n\n Чтобы выводы первой и второй задачи стояли отдельно в консоли

# 2
print("2 exercise:")

list = [1, 2, 3, 4, 5, 1, 2]  # 1 and 2 are repeating

unique = set()
repeat = set()

for i in list:
    if i not in unique:
        unique.add(i)
    else:
        repeat.add(i)

unique = unique - repeat

print(unique, end="\n\n")

# 3
print("3 exercise:")

animals = {"cat_name": "Tom", "cat_type": "cat", "cat_age": "3 years",
           "dog_name": "Rex", "dog_type": "dog", "dog_age": "6 years",
           "fish_name": "Bob", "fish_type": "fish", "fish_age": "1 year",
           "horse_name": "Alex", "horse_type": "horse", "horse_age": "20 years"}

print("Cat information:")

for key, value in animals.items():
    if key.startswith("cat"):
        print(value)

print("\nDog information:")

for key, value in animals.items():
    if key.startswith("dog"):
        print(value)

print("\nFish information:")

for key, value in animals.items():
    if key.startswith("fish"):
        print(value)

print("\nHorse information:")

for key, value in animals.items():
    if key.startswith("horse"):
        print(value)
