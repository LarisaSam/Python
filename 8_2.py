#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.#
#
# class Div_ByNull():
#     def __init__(self, dividend,  divisor):
#         self.dividend = dividend
#         self.denominator = divisor
#
#     @staticmethod
#     def divide_by_null(dividend,  divisor):
#         try:
#             return (dividend /  divisor)
#         except:
#             return (f"Деление на ноль недопустимо")
#
#
# div = Div_ByNull(15, 100)
# print(Div_ByNull.divide_by_null(15, 5))
# print(Div_ByNull.divide_by_null(15, 0))
# print(Div_ByNull.divide_by_null(15, 0.1))
# print(div.divide_by_null(100, 0))

class Div_ByNull(Exception):
    def __init__(self, dividend,  divisor):
        self.dividend = dividend
        self.denominator = divisor

    @staticmethod
    def divide_by_null(dividend,  divisor):
        try:
            return (dividend /  divisor)
        except:
            return (f"Деление на ноль недопустимо")


div = Div_ByNull(15, 100)
print(Div_ByNull.divide_by_null(15, 5))
print(Div_ByNull.divide_by_null(15, 0))
print(Div_ByNull.divide_by_null(15, 0.1))
print(div.divide_by_null(100, 0))
