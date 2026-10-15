# perf_counter используется для измерения длительности выполнения кода.
import time
# contextmanager позволяет создать контекстный менеджер через генератор.
from contextlib import contextmanager


# Первый вариант контекстного менеджера реализован классом.
class cm_timer_1:
    # Вызывается при входе в блок with и запоминает момент начала.
    def __enter__(self):
        self.start_time = time.perf_counter()

    # Вызывается при выходе из блока with, в том числе при исключении.
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        # Разница показаний счётчика — время выполнения в секундах.
        print(f"time: {end_time - self.start_time}")


# Второй вариант реализован функцией с декоратором contextmanager.
@contextmanager
def cm_timer_2():
    start_time = time.perf_counter()

    try:
        # На время выполнения блока with управление передаётся вызывающему коду.
        yield
    # finally обеспечивает вывод времени даже при ошибке внутри блока.
    finally:
        end_time = time.perf_counter()
        print(f"time: {end_time - start_time}")


# В обоих примерах измеряется пауза длительностью одну секунду.
if __name__ == "__main__":
    print("cm_timer_1:")
    with cm_timer_1():
        time.sleep(1)

    print("\ncm_timer_2:")
    with cm_timer_2():
        time.sleep(1)