from .rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "{}: сторона = {}, цвет = {}, площадь = {}".format(
            self.get_figure_type(),
            self.width,
            self.color.color,
            self.area()
        )