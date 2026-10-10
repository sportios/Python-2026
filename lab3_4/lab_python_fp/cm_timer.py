import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        print(f"time: {end_time - self.start_time}")


@contextmanager
def cm_timer_2():
    start_time = time.perf_counter()

    try:
        yield
    finally:
        end_time = time.perf_counter()
        print(f"time: {end_time - start_time}")


if __name__ == "__main__":
    print("cm_timer_1:")
    with cm_timer_1():
        time.sleep(1)

    print("\ncm_timer_2:")
    with cm_timer_2():
        time.sleep(1)