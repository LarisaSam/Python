#4. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('f_5_4.txt', "w+") as numbers:

    line = input('Введите числа, разделенные пробелом')
    numbers.write(line)

    numbers.seek(0)

    my_line = numbers.readline().split()
    print(my_line)
    sum_numbers = 0
    for el in my_line:
        sum_numbers+=int(el)

    print(f'Cумма чисел: {sum_numbers}')

