class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self._current_value = self.start

    def __next__(self):
        value = self._current_value
        if value >= self.stop:
            raise StopIteration
        self._current_value += 1
        return value

    def __iter__(self):
        return self
