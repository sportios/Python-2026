# Генератор получает список словарей и названия полей для извлечения.
def field(items, *args):
    # Необходимо указать хотя бы одно название поля.
    assert len(args) > 0

    # Последовательно обрабатываем каждый словарь из входного списка.
    for item in items:
        # Для одного поля возвращаем непосредственно его значение.
        if len(args) == 1:
            value = item.get(args[0])

            # Пропускаем отсутствующие значения и значения None.
            if value is not None:
                yield value

        else:
            # Для нескольких полей формируем новый словарь только с непустыми значениями.
            result = {
                key: item[key]
                for key in args
                if key in item and item[key] is not None
            }

            # Не возвращаем пустой словарь, если подходящих полей нет.
            if result:
                yield result


# Пример использования генератора для одного и нескольких ключей.
if __name__ == "__main__":
    goods = [
        {
            "title": "Ковер",
            "price": 2000,
            "color": "green"
        },
        {
            "title": "Диван для отдыха",
            "color": "black"
        },
        {
            "title": None,
            "price": 5000,
            "color": "white"
        }
    ]

    print("Один аргумент:")
    for value in field(goods, "title"):
        print(value)

    print("\nНесколько аргументов:")
    for value in field(goods, "title", "price"):
        print(value)