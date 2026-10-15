# Декоратор печатает имя функции и полученный результат.
def print_result(func):
    # Обёртка принимает любые позиционные и именованные аргументы.
    def wrapper(*args, **kwargs):
        # Вызываем исходную функцию и сохраняем её результат.
        result = func(*args, **kwargs)

        # Выводим имя исходной функции, а не имя обёртки.
        print(func.__name__)

        # Элементы списка печатаются по одному на строку.
        if isinstance(result, list):
            for item in result:
                print(item)

        # Для словаря выводим пары «ключ = значение».
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")

        else:
            # Для остальных типов используем обычный вывод.
            print(result)

        # Декоратор не изменяет возвращаемое значение функции.
        return result

    return wrapper


# Тестовые функции демонстрируют обработку разных типов результата.
@print_result
def test_1():
    return 1


@print_result
def test_2():
    return "iu5"


@print_result
def test_3():
    return {"a": 1, "b": 2}


@print_result
def test_4():
    return [1, 2]


# Последовательный запуск тестов декоратора.
if __name__ == "__main__":
    print("!!!!!!!!")
    test_1()
    test_2()
    test_3()
    test_4()