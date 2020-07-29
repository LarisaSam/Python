#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

    def  display_worker(self):
        print(f" Имя: {self.name} Фамилия: {self.surname} доход: {self.income}")

inst_1 = Worker("Иван", "Иванов", "директор", 1000)
inst_2 = Worker("Петр", "Петров", "бухгалтер", 500)
inst_3 = Worker("Сергей", "Сергеев", "менеджер", 300)

inst_1.display_worker()
inst_2.display_worker()
inst_3.display_worker()

# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Полный доход {self.income}")

inst_1_1 = Position("Иван", "Петров","директор", 1000)
inst_2_1 = Position("Петр", "Петров", "бухгалтер", 500)
inst_3_1 = Position("Сергей", "Сергеев", "менеджер", 300)

inst_1_1.get_full_name()
inst_2_1.get_full_name()
inst_3_1.get_full_name()

inst_1_1.get_total_income()
inst_2_1.get_total_income()
inst_3_1.get_total_income()
