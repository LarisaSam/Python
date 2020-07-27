#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file5_2 = open('f_5_2.txt')
line = 0
for i in my_file5_2:
    line+=1

    signal = 0 #нахождение вне слова
    word = 0
    for j in i:
        if j != ' ' and signal == 0:
            word+=1
            signal = 1
        elif j == ' ':
            signal = 0

    print(f"{i} Количество слов в строке:>> {word}")

print('Количество строк:>>', line)
my_file5_2.close()


