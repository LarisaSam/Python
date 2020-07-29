# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

class TrafficLight:
    __color: str

    def __init__(self, color):
        self.color = color

    def running(self):
        print(self.color)

red_mode = TrafficLight("red")
yellow_mode = TrafficLight("yellow")
green_mode = TrafficLight("green")

import time
for i in range(2):
    red_mode.running()
    time.sleep(7)
    yellow_mode.running()
    time.sleep(2)
    green_mode.running()
    time.sleep(4)
    i+=1







