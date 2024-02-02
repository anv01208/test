# 1

with open('text.txt', 'r') as file:
    content = file.read()
    words = content.split()
    modified_words = []

    for word in words:
        if 'З' in word or 'з' in word:
            modified_words.append('***')
        else:
            modified_words.append(word)

    modified_text = ' '.join(modified_words)

with open('output1.txt', 'w') as output_file:
    output_file.write(modified_text)

print('Конец программы!')

# 2

try:
    with open('fake_file.txt', 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Файл не найден")

else:
    print("'Else' выполняется если нет 'except'")

finally:
    print("'Finally' выполняется всегда!")
