n, k = map(int, input().split())

cnt = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        t = k - a - b
        if 1 <= t and t <= n:
            cnt += 1

print(cnt)
