from math import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_multiple(numbers):
    return reduce(lcm, numbers)


n = int(input())
a = list(map(int, input().split()))
print(lcm_multiple(a))
