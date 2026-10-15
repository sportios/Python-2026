# Итератор возвращает элементы в исходном порядке, исключая повторы.
class Unique:
    def __init__(self, items, **kwargs):
        # iter позволяет одинаково работать со списками и генераторами.
        self.items = iter(items)
        # Необязательный параметр определяет, учитывать ли регистр строк.
        self.ignore_case = kwargs.get("ignore_case", False)
        # Множество хранит значения, которые уже встречались.
        self.used = set()

    # Получение следующего ещё не встречавшегося элемента.
    def __next__(self):
        while True:
            # При завершении источника StopIteration завершит и этот итератор.
            item = next(self.items)

            # Для сравнения строк без учёта регистра используем нижний регистр.
            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item

            # Сохраняем ключ для проверки, но возвращаем исходный элемент.
            if key not in self.used:
                self.used.add(key)
                return item

    # Сам объект реализует протокол итератора.
    def __iter__(self):
        return self


# Проверка удаления повторов для чисел и строк.
if __name__ == "__main__":
    data = [1, 1, 1, 2, 2, 3, 3]
    print("Числа:")
    for item in Unique(data):
        print(item)

    data = ["a", "A", "b", "B", "a", "A", "b", "B"]

    print("\nСтроки, ignore_case=False:")
    for item in Unique(data):
        print(item)

    print("\nСтроки, ignore_case=True:")
    for item in Unique(data, ignore_case=True):
        print(item)