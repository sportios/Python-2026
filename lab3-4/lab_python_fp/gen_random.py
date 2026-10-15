# randint генерирует целое число, включая обе границы диапазона.
from random import randint


# Генератор лениво выдаёт num_count случайных чисел в заданных границах.
def gen_random(num_count, begin, end):
    # Символ _ используется, поскольку номер итерации не нужен.
    for _ in range(num_count):
        # yield выдаёт очередное число без формирования списка целиком.
        yield randint(begin, end)


# Проверка: вывод пяти случайных чисел от 1 до 3.
if __name__ == "__main__":
    print("Случайные числа:")
    for value in gen_random(5, 1, 3):
        print(value)