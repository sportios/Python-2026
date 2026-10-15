# Импортируем класс Console из внешнего пакета rich для оформления вывода.
from rich.console import Console

# Импортируем разработанные классы геометрических фигур из пакета lab_python_oop.
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    # N — номер варианта; в данном примере используется значение 1.
    n = 1

    # Создаем прямоугольник, круг и квадрат с заданными размерами и цветами.
    rectangle = Rectangle(n, n, "синий")
    circle = Circle(n, "зеленый")
    square = Square(n, "красный")

    # Выводим информацию о фигурах: размеры, цвет и вычисленную площадь.
    # Метод print использует строку, сформированную методом __repr__ каждого класса.
    print(rectangle)
    print(circle)
    print(square)

    # Демонстрируем работу внешнего пакета rich, установленного через pip.
    console = Console()
    console.print("Внешний пакет rich работает!")


# Запускаем main() только при непосредственном запуске файла main.py.
if __name__ == "__main__":
    main()
