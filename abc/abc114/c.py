import sys

sys.setrecursionlimit(10**6)

N = int(input())
M = len(str(N))


def is_ok(x):
    return len(set(x)) == 3


def f(a, seq):
    if a and int(a) > N:
        return
    if is_ok(a):
        seq.append(a)

    for j in ["3", "5", "7"]:
        f(a + j, seq)

    return seq


seq = f("", [])
print(len(seq))
