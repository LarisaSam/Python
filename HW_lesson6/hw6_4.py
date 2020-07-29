#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed: str
    color: str
    name: str
    is_police: bool

    def __init__(self,speed, color, name, is_police, side):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.side = side

    def go(self):
        if self.speed != 0:
            print("Машина поехала")
        else:
            print("Машина стоит")

    def stop(self):
        if self.speed == 0:
            print("Машина остановилась")
        else:
            print("Машина не остановилась")

    def turn(self):
        if self.side == "right":
            print('Машина поворачивает направо')
        elif self.side == "left":
                print('Машина поворачивает налево')
        else:
            print("Машина не поворачивает")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")


inst = Car(7, "bleak", "oka", True, "left")
inst1 = Car(0, "red", "ford", False,"right" )

inst.go()
inst1.go()
inst.stop()
inst1.stop()
inst.show_speed()


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение разрешенной скорости!")

townCar_1 = TownCar(50, 'bleak', 'Reno', '', "right")
townCar_2 = TownCar(70, 'bleak', 'Reno', '', "left")

townCar_1.go()
townCar_1.stop()
townCar_1.show_speed()
townCar_2.show_speed()
townCar_1.turn()


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение разрешенной скорости!")


workCar_1 = WorkCar(0, 'bleak', 'Kamaz', '', "right")
workCar_2 = WorkCar(50, 'bleak', 'Gazel', '', " ")

workCar_1.go()
workCar_1.stop()
workCar_1.show_speed()
workCar_2.show_speed()
workCar_2.turn()


class SportCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed < 200:
            print("Не слишком ли медленно мы едем?.")

sportCar1 = SportCar(200, "red", "Ferrary", True, "left")
sportCar2 = SportCar(150, "wihte", "McLaren", False, "")

sportCar1.turn()
sportCar2.go()


class PoliceCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 80:
            print("Нарушаем?")

policeCar1 = PoliceCar(100, "red", "Mersedes", True, "left")
policeCar2 = PoliceCar(0, "wihte", "Lada", False, " ")

policeCar1.show_speed()
policeCar2.stop()
