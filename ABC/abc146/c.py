a, b, x = map(int, input().split())


def is_ok(n):
    return a * n + b * len(str(n)) <= x


ok, ng = 0, 10**9 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
