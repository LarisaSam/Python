#3.b.Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.При этом английские
# числительные должны заменяться на русские.Новый блок строк должен записываться в новый текстовый файл.

my_file1 = open('f_5_3_b(1).txt')

translation = {'One': 'Один', "Two": 'Два', 'Three': 'Три', 'Four': 'Четыре'}

for line in my_file1:
    key, dash, value = line.split()
    key = translation[key]
    print(key, dash, value)

    with open("f_5_3_b(2).txt", "a") as my_file2:
        print(key, dash, value, file=my_file2) #запись в файл f_5_3_b(2).txt

my_file1.close()
