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

    # Если параметр не задан или введён неверно — ввод с клавиатуры
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


def solve_biquadratic(a, b, c):
    # Биквадратное уравнение:
    # A*x^4 + B*x^2 + C = 0
    #
    # Делаем замену:
    # y = x^2
    #
    # Получаем:
    # A*y^2 + B*y + C = 0

    discriminant = b ** 2 - 4 * a * c

    print(f"Дискриминант D = {discriminant}")

    # Находим корни уравнения относительно y
    if discriminant < 0:
        return []

    if discriminant == 0:
        y_roots = [-b / (2 * a)]
    else:
        sqrt_d = math.sqrt(discriminant)

        y1 = (-b + sqrt_d) / (2 * a)
        y2 = (-b - sqrt_d) / (2 * a)

        y_roots = [y1, y2]

    # Теперь из y = x^2 находим действительные x
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
    print("A*x^4 + B*x^2 + C = 0")

    a = get_coefficient(1, "A", non_zero=True)
    b = get_coefficient(2, "B")
    c = get_coefficient(3, "C")

    roots = solve_biquadratic(a, b, c)

    if len(roots) == 0:
        print("Действительных корней нет.")
    else:
        print("Действительные корни:")

        for i, root in enumerate(roots, 1):
            print(f"x{i} = {root}")


if __name__ == "__main__":
    main()