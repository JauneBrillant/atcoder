n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
cd = [tuple(map(int, input().split())) for _ in range(k)]

ans = 0
for bit in range(1 << k):
    plate = [False] * (n + 1)
    for i in range(k):
        if bit & (1 << i):
            plate[cd[i][0]] = True
        else:
            plate[cd[i][1]] = True

    cnt = 0
    for a, b in ab:
        if plate[a] and plate[b]:
            cnt += 1

    ans = max(ans, cnt)

print(ans)
