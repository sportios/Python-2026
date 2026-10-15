# Загрузка данных о вакансиях из JSON-файла.
import json
import sys

# Используем инструменты, реализованные в предыдущих заданиях.
from field import field
from unique import Unique
from gen_random import gen_random
from print_result import print_result
from cm_timer import cm_timer_1


# Путь к файлу с данными передаётся первым аргументом командной строки.
path = sys.argv[1]

# Контекстный менеджер автоматически закрывает файл после чтения.
with open(path, encoding="utf-8") as f:
    data = json.load(f)


# f1: извлекаем названия вакансий, исключаем дубли без учёта регистра
# и сортируем результат в алфавитном порядке.
@print_result
def f1(arg):
    return sorted(Unique(field(arg, "job-name"), ignore_case=True), key=str.lower)


# f2: оставляем только профессии, начинающиеся со слова «программист».
@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"), arg))


# f3: с помощью map дополняем каждую профессию указанием опыта Python.
@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


# f4: формируем строки с профессиями и случайными зарплатами.
@print_result
def f4(arg):
    # Генерируем по одной зарплате от 100 000 до 200 000 руб. на вакансию.
    salaries = gen_random(len(arg), 100000, 200000)
    # zip попарно объединяет название профессии и соответствующую зарплату.
    return [
        f"{profession}, зарплата {salary} руб."
        for profession, salary in zip(arg, salaries)
    ]


# Выполняем цепочку f1 → f2 → f3 → f4 и измеряем общее время.
if __name__ == "__main__":
    with cm_timer_1():
        f4(f3(f2(f1(data))))