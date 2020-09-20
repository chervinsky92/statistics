from math import sqrt

# from statistics import mean
def mean(data):
    return sum(data) / len(data)

# from statistics import median
def median(data):
    data.sort()
    n = len(data)
    mid = n // 2

    if n % 2: # != 0, therefore odd
        return (data[mid])
    return (data[mid-1] + data[mid]) / 2 # even

# from statistics import mode
# will only return 1 of the modes if there are multiple
def mode(data):
    mode_count = 0
    for i in range(len(data)):
        current_count = data.count(data[i])
        if current_count > mode_count:
            mode = data[i]
            mode_count = current_count
    return mode

# from statistics import variance
def variance(data):
    mu = mean(data)
    return mean([(x-mu)**2 for x in data])

# from statistics import stdev
def standard_deviation(data):
    return sqrt(variance(data))