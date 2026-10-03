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

    # Если параметра нет или он некорректен — ввод с клавиатуры
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


def sign(value):
    """Возвращает знак числа."""
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0


def get_y_roots(a, b, c):
    """Вычисление корней после замены y = x^2."""

    discriminant = b ** 2 - 4 * a * c

    match sign(discriminant):
        case -1:
            return discriminant, ()

        case 0:
            y = -b / (2 * a)
            return discriminant, (y,)

        case 1:
            sqrt_d = math.sqrt(discriminant)

            y1 = (-b + sqrt_d) / (2 * a)
            y2 = (-b - sqrt_d) / (2 * a)

            return discriminant, (y1, y2)


def y_to_x(y):
    """Преобразование y = x^2 в действительные корни x."""

    match sign(y):
        case -1:
            return ()

        case 0:
            return (0.0,)

        case 1:
            root = math.sqrt(y)
            return (root, -root)


def solve_biquadratic(a, b, c):
    discriminant, y_roots = get_y_roots(a, b, c)

    roots = tuple(
        x
        for y in y_roots
        for x in y_to_x(y)
    )

    return discriminant, roots


def main():
    print("Решение биквадратного уравнения")
    print("Функциональная версия")
    print("A*x^4 + B*x^2 + C = 0")

    a = get_coefficient(1, "A", non_zero=True)
    b = get_coefficient(2, "B")
    c = get_coefficient(3, "C")

    discriminant, roots = solve_biquadratic(a, b, c)

    print(f"Дискриминант D = {discriminant}")

    match len(roots):
        case 0:
            print("Действительных корней нет.")

        case _:
            print("Действительные корни:")

            for i, root in enumerate(roots, 1):
                print(f"x{i} = {root}")


if __name__ == "__main__":
    main()