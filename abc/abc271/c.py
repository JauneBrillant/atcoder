from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(set(a))
same = n - len(sorted_a)
a.sort()


def cond(x):
    t = bisect_right(sorted_a, x)
    return t + (same + len(sorted_a) - t) // 2 >= x


ok, ng = 0, n + 1
while ok + 1 < ng:
    mi = (ok + ng) // 2
    if cond(mi):
        ok = mi
    else:
        ng = mi

print(ok)
