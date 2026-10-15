# Исходный список содержит положительные, отрицательные числа и ноль.
data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]


if __name__ == "__main__":
    # Сортировка по убыванию модуля с передачей встроенной функции abs.
    result = sorted(data, key=abs, reverse=True)
    print("Без lambda:")
    print(result)

    # Тот же порядок с анонимной lambda-функцией в качестве ключа.
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print("\nС lambda:")
    print(result_with_lambda)