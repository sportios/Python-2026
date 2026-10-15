# Класс отвечает за хранение и изменение цвета геометрической фигуры.
class FigureColor:
    def __init__(self, color):
        # Сохраняем переданное значение во внутреннем атрибуте.
        self._color = color

    @property
    def color(self):
        # Геттер позволяет получить цвет через свойство color.
        return self._color

    @color.setter
    def color(self, value):
        # Сеттер позволяет изменить цвет через то же свойство.
        self._color = value
