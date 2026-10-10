from random import randint


def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield randint(begin, end)


if __name__ == "__main__":
    print("Случайные числа:")
    for value in gen_random(5, 1, 3):
        print(value)