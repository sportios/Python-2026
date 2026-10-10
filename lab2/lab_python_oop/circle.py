import math

from .geometric_figure import GeometricFigure
from .figure_color import FigureColor


class Circle(GeometricFigure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return "{}: радиус = {}, цвет = {}, площадь = {}".format(
            self.get_figure_type(),
            self.radius,
            self.color.color,
            self.area()
        )