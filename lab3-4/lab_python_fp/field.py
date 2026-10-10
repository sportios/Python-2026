def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            value = item.get(args[0])

            if value is not None:
                yield value

        else:
            result = {
                key: item[key]
                for key in args
                if key in item and item[key] is not None
            }

            if result:
                yield result


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