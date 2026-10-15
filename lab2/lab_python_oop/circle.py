# Модуль math нужен для математической константы pi.
import math

# Импортируем абстрактный базовый класс и класс для хранения цвета.
from .geometric_figure import GeometricFigure
from .figure_color import FigureColor


# Круг является отдельной реализацией геометрической фигуры.
class Circle(GeometricFigure):
    # Название фигуры хранится в атрибуте класса.
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        # Сохраняем радиус и создаем объект для хранения цвета круга.
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        # Площадь круга вычисляется по формуле S = pi * r^2.
        return math.pi * self.radius ** 2

    @classmethod
    def get_figure_type(cls):
        # Возвращаем название фигуры из атрибута класса.
        return cls.FIGURE_TYPE

    def __repr__(self):
        # Выводим основные характеристики круга в виде одной строки.
        return "{}: радиус = {}, цвет = {}, площадь = {}".format(
            self.get_figure_type(),
            self.radius,
            self.color.color,
            self.area()
        )
