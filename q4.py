
def moreStats(func):
    def wrapper(*args, **kwargs):
        # Calculate statistics
        result = func(*args, **kwargs)
        count = len(result)
        total = sum(result)
        average = total / count
        maximum = max(result)
        print(count)
        print(total)
        print(average)
        print(maximum)
    return wrapper

@moreStats
def printStats(t):
    file = open(t, "r")
    numbers = []
    for line in file:
        numbers += list(map(int, line.split()))
    return numbers

printStats("python.txt")
