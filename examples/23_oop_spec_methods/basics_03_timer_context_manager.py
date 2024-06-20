import time


class RunningTime:
    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("__enter__")
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__", exc_type, exc_value, traceback)
        self.stop = time.time()
        print(f"Running time: {self.stop - self.start}")

r = RunningTime()
print("#"*40)

with r:
    print("TEST")
    time.sleep(3)
