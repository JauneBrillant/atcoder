N = int(input())
xy = sorted(tuple(map(int, input().split())) for _ in range(N))
st = set(xy)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        x1, y1, x2, y2 = *xy[i], *xy[j]
        if x1 != x2 and y1 != y2:
            if (x1, y2) in st and (x2, y1) in st:
                ans += 1

print(ans // 2)
