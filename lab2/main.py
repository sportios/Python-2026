from rich.console import Console

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    n = 1

    rectangle = Rectangle(n, n, "синий")
    circle = Circle(n, "зеленый")
    square = Square(n, "красный")

    print(rectangle)
    print(circle)
    print(square)

    console = Console()
    console.print("Внешний пакет rich работает!")


if __name__ == "__main__":
    main()