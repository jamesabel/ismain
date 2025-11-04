import time

start = time.perf_counter()


def main():
    return


if __name__ == "__main__":
    main()

stop = time.perf_counter()

print(f"Execution time: {1000 * (stop - start):.3f} mS")
