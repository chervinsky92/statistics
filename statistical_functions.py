from math import sqrt
import random

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

# add a number to an existing mean
def incremental_mean(oldmean, n, x):
    sum = oldmean * n
    return (sum + x) / (n + 1)

# compute the likelihood of observing a sequence of results in a given order
# dist: dictionary of results and their corresponding probabilities
# data: string/list of desired sequence
def likelihood(dist, data):
    l = 1.0
    for item in data:
        l *= dist[item]
    return l
# print(likelihood({'A':0.2,'B':0.2,'C':0.2,'D':0.2,'E':0.2}, 'ABCEDDECAB'))
# print(likelihood({'Good':0.6,'Bad':0.2,'Indifferent':0.2}, ['Good','Bad','Indifferent','Good','Good','Bad']))

# simulate flipping N fair coins
# int(True) -> 1 
# int(False) -> 0
def flip(N):
    return [random.random() > 0.5 for x in range(N)]

# simulate sets of coin flips
def sample(N_flips, N_sets):
    return [mean(flip(N_flips)) for x in range(N_sets)]
# print(sample(1000, 1000))