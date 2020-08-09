#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные
# и заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списк

class Check_Number:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите элемент списка, нажмите Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Это не число")

                y_or_n = input(f'Продолжить ввод? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    break
                break


try_except = Check_Number(1)
print(try_except.my_input())
