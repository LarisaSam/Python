#Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def drav(self):
        print(f"Запуск отрисовки: {self.title}")

inst = Stationery("stationery: some")
inst.drav()

class Pen(Stationery):

    def drav(self):
        super().drav()
        print(f"Запуск отрисовки: {self.title}: Pen")

inst1 = Pen("stationery:")
inst1.drav()

class Pencil(Stationery):

    def drav(self):
        super().drav()
        print(f"Запуск отрисовки: {self.title} Pencil")

inst2 = Pencil("stationery:")
inst2.drav()


class Handle(Stationery):

    def drav(self):
        super().drav()
        print(f"Запуск отрисовки: {self.title} Handle")

inst3 = Handle("stationery:")
inst3.drav()






# def __init__(self, title, exact_title):
    #     super().__init__(title)
    #     self.exact_title = exact_title
    #
    # def drav(self):
    #     super().drav()
    #     print(f"Запуск отрисовки: {self.title} - {self.exact_title}")
#
# inst_1_1 = Pen("stationery:", "Pen")
# inst_1_1.drav()
#




