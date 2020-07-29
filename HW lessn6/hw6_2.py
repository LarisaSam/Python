# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _lenth: int
    _width: int

    def __init__(self, lenth, width, mass_1sm, thickness):
        self.lenth = lenth
        self.width = width
        self.mass_1sm = mass_1sm
        self.thickness = thickness

    # def area(self):
    #     self.ar = self._lenth * self._width

    def count(self):
        self.mass = self.lenth * self.width * self.mass_1sm  * self.thickness
        print(f"Требуемая масса асфальта - {self.mass/1000} тонн")


mass_asphalt = Road(lenth=20, width= 5000, mass_1sm=25, thickness=5)

# mass_asphalt.area()
mass_asphalt.count()



