# Импортируем абстрактный базовый класс и класс для хранения цвета.
from .geometric_figure import GeometricFigure
from .figure_color import FigureColor


# Прямоугольник наследуется от общего класса геометрических фигур.
class Rectangle(GeometricFigure):
    # Название фигуры задается атрибутом класса, общим для его экземпляров.
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        # Сохраняем геометрические размеры фигуры.
        self.width = width
        self.height = height
        # Создаем отдельный объект, отвечающий за цвет прямоугольника.
        self.color = FigureColor(color)

    def area(self):
        # Реализуем абстрактный метод: площадь равна ширине, умноженной на высоту.
        return self.width * self.height

    @classmethod
    def get_figure_type(cls):
        # Возвращаем название фигуры из атрибута класса.
        return cls.FIGURE_TYPE

    def __repr__(self):
        # Формируем строковое представление с названием, размерами, цветом и площадью.
        # Цвет читаем через свойство объекта FigureColor.
        return "{}: ширина = {}, высота = {}, цвет = {}, площадь = {}".format(
            self.get_figure_type(),
            self.width,
            self.height,
            self.color.color,
            self.area()
        )
