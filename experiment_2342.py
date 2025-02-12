from collections import defaultdict
from algorithms import digsum

# some data for 2342_max_sum_of_a_pair_with_equal_sum_of_digits.py

dig10sum = lambda d: digsum(d, 10)

n_min = 0
n_max = 10**6
d = defaultdict(list)
completion_prev = - 1
for n in range(n_min, n_max + 1):
    completion = (n * 100) // n_max
    if completion != completion_prev:
        print(f'{completion}%', end='\r')
    completion_prev = completion
    k = dig10sum(n)
    d[k].append(n) # group numbers by the sum of their digits
MINMAXSUM = defaultdict(int) # this map matches the sum of digits to the minimum and maximum sum of two numbers whose sum of digits equals k
for k in d:
    max1 = max(d[k]) # find the max number which sum of digits equals k
    min1 = min(d[k]) # find the min number which sum of digits equals k
    d[k].remove(max1) # remove max number from the set to find the next max number in the set
    max2 = max(d[k]) if len(d[k]) > 0 else 0 # this number is closest to the max number and which sum of digits equals k
    max_possible_sum = max1 + max2 # this is the max possible sum of two numbers whose sum of digits equals l
    d[k].append(max1) # return back max number which sum of digits is equal k
    d[k].remove(min1) # remove min number which sum of digits is equal k to find the next min number in the set
    min2 = min(d[k]) if len(d[k]) > 0 else 0 # this number is closest to the min number and which sum of digits equals k 
    min_possible_sum = min1 + min2 # this is the min possible sum of two numbers whose sum of digits equals k
    MINMAXSUM[k] = [min_possible_sum, max_possible_sum]
    del d[k][:] # free mem
for k in MINMAXSUM:
    print(f'{k}: {MINMAXSUM[k]}')
