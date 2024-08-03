n, w = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(reverse=True)

ans = 0
total_g = 0
for a, b in ab:
    while b > 0 and total_g < w:
        ans += a
        b -= 1
        total_g += 1

print(ans)
