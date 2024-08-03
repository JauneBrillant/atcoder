from bisect import bisect_right

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()


def is_ok(x):
    cnt = 0
    for ai in a:
        cnt += bisect_right(b, x // ai)
    return cnt >= k


ng, ok = -1, 10**18 + 1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
