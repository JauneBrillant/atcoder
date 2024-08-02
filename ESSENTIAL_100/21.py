n = int(input())
hs = []
for _ in range(n):
    a, b = map(int, input().split())
    hs.append((a, b))


def is_ok(height):
    times = []
    for h, s in hs:
        if height < h:
            return False
        times.append((height - h) // s)
    times.sort()

    for i in range(n):
        if times[i] < i:
            return False
    return True


ng, ok = 0, 10**20
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
