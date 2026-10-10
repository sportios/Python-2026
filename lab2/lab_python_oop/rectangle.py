from .geometric_figure import GeometricFigure
from .figure_color import FigureColor


class Rectangle(GeometricFigure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return "{}: ширина = {}, высота = {}, цвет = {}, площадь = {}".format(
            self.get_figure_type(),
            self.width,
            self.height,
            self.color.color,
            self.area()
        )