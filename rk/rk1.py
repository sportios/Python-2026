
from operator import itemgetter


class DataColumn:
    """Колонка данных."""

    def __init__(self, id, name, size_kb, table_id):
        self.id = id
        self.name = name
        self.size_kb = size_kb
        self.table_id = table_id


class DataTable:
    """Таблица данных."""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ColumnTable:
    """Связь многие-ко-многим."""

    def __init__(self, table_id, column_id):
        self.table_id = table_id
        self.column_id = column_id


# Таблицы данных
tables = [
    DataTable(1, 'Архив заказов'),
    DataTable(2, 'Аналитика продаж'),
    DataTable(3, 'Клиенты'),
    DataTable(4, 'Товары'),
]

# Колонки данных
columns = [
    DataColumn(1, 'Код заказов', 12, 1),
    DataColumn(2, 'Дата', 10, 1),
    DataColumn(3, 'Сумма', 16, 2),
    DataColumn(4, 'Код клиентов', 8, 3),
    DataColumn(5, 'Код товаров', 20, 4),
]

# Связи многие-ко-многим
columns_tables = [
    ColumnTable(1, 1),
    ColumnTable(1, 2),
    ColumnTable(1, 4),
    ColumnTable(2, 1),
    ColumnTable(2, 3),
    ColumnTable(2, 5),
    ColumnTable(3, 4),
    ColumnTable(4, 5),
]


def main():
    # Соединение один-ко-многим
    one_to_many = [
        (col.name, col.size_kb, table.name)
        for table in tables
        for col in columns
        if col.table_id == table.id
    ]

    # Соединение многие-ко-многим
    many_to_many_temp = [
        (table.name, relation.table_id, relation.column_id)
        for table in tables
        for relation in columns_tables
        if table.id == relation.table_id
    ]

    many_to_many = [
        (col.name, col.size_kb, table_name)
        for table_name, table_id, column_id in many_to_many_temp
        for col in columns
        if col.id == column_id
    ]

    # Задание Д1
    # Колонки, названия которых заканчиваются на "ов"
    print('Задание Д1')

    res_11 = [
        (col_name, table_name)
        for col_name, _, table_name in one_to_many
        if col_name.endswith('ов')
    ]

    print(res_11)

    # Задание Д2
    # Средний объем колонок в каждой таблице
    print('\nЗадание Д2')

    res_12_unsorted = []

    for table in tables:
        table_columns = list(filter(
            lambda item: item[2] == table.name,
            one_to_many
        ))

        if table_columns:
            sizes = [
                size for _, size, _ in table_columns
            ]

            mean_size = sum(sizes) / len(sizes)

            res_12_unsorted.append(
                (table.name, mean_size)
            )

    res_12 = sorted(
        res_12_unsorted,
        key=itemgetter(1),
        reverse=True
    )

    print(res_12)

    # Задание Д3
    # Таблицы на букву "А" и связанные с ними колонки
    print('\nЗадание Д3')

    res_13 = {}

    for table in tables:
        if table.name.startswith('А'):
            table_columns = list(filter(
                lambda item: item[2] == table.name,
                many_to_many
            ))

            res_13[table.name] = [
                name for name, _, _ in table_columns
            ]

    print(res_13)


if __name__ == '__main__':
    main()
