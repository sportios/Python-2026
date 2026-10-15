# ABC позволяет создать абстрактный базовый класс, а abstractmethod — абстрактный метод.
from abc import ABC, abstractmethod


# Общий абстрактный класс для всех геометрических фигур.
# Экземпляр GeometricFigure напрямую создать нельзя: сначала нужно реализовать area().
class GeometricFigure(ABC):

    @abstractmethod
    def area(self):
        # Каждый конкретный класс фигуры должен определить собственный расчет площади.
        pass
