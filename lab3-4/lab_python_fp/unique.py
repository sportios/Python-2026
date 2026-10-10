class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get("ignore_case", False)
        self.used = set()

    def __next__(self):
        while True:
            item = next(self.items)

            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item

            if key not in self.used:
                self.used.add(key)
                return item

    def __iter__(self):
        return self


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