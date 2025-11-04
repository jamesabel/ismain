import time

start = time.perf_counter()

from ismain import is_main


def main():
    return


if is_main():
    main()

stop = time.perf_counter()

print(f"Execution time: {1000 * (stop - start):.3f} mS")
