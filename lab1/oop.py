import sys
import math


def get_coefficient(index, name, non_zero=False):
    # Сначала пробуем получить коэффициент из командной строки
    if len(sys.argv) > index:
        try:
            value = float(sys.argv[index])

            if non_zero and value == 0:
                print(f"Коэффициент {name} не должен быть равен нулю.")
            else:
                return value

        except ValueError:
            print(
                f"Некорректное значение коэффициента {name} "
                f"в командной строке."
            )

    # Если параметр отсутствует или некорректен — вводим с клавиатуры
    while True:
        try:
            value = float(input(f"Введите коэффициент {name}: "))

            if non_zero and value == 0:
                print(
                    f"Коэффициент {name} не должен быть равен нулю. "
                    "Попробуйте снова."
                )
                continue

            return value

        except ValueError:
            print(
                f"Некорректное значение для коэффициента {name}. "
                "Попробуйте снова."
            )


class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        discriminant = self.discriminant()

        print(f"Дискриминант D = {discriminant}")

        if discriminant < 0:
            return []

        if discriminant == 0:
            y_roots = [-self.b / (2 * self.a)]
        else:
            sqrt_d = math.sqrt(discriminant)

            y1 = (-self.b + sqrt_d) / (2 * self.a)
            y2 = (-self.b - sqrt_d) / (2 * self.a)

            y_roots = [y1, y2]

        roots = []

        for y in y_roots:
            if y > 0:
                roots.append(math.sqrt(y))
                roots.append(-math.sqrt(y))

            elif y == 0:
                roots.append(0.0)

        return roots


def main():
    print("Решение биквадратного уравнения")
    print("Объектно-ориентированная версия")
    print("A*x^4 + B*x^2 + C = 0")

    a = get_coefficient(1, "A", non_zero=True)
    b = get_coefficient(2, "B")
    c = get_coefficient(3, "C")

    equation = BiquadraticEquation(a, b, c)

    roots = equation.solve()

    if len(roots) == 0:
        print("Действительных корней нет.")
    else:
        print("Действительные корни:")

        for i, root in enumerate(roots, 1):
            print(f"x{i} = {root}")


if __name__ == "__main__":
    main()