A, B, C, X, Y = map(int, input().split())
ans = 10**9

ab = [i for i in range(max(X, Y) * 2 + 9) if i % 2 == 0]
for k in ab:
    i = X - k // 2
    j = Y - k // 2
    if i < 0 or j < 0:
        continue
    ans = min(ans, A * i + B * j + C * k)

print(ans)
