n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()


def is_ok(x):
    total = sum(min(x, ai) for ai in a)
    return total <= m


ok, ng = -1, m + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
if ok == m:
    print("infinite")
else:
    print(ok)
