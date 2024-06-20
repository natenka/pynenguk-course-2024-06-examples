

def my_range(start, stop):
    current_value = start
    while current_value < stop:
        yield current_value
        current_value += 1
