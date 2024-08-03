n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

ok = True
for i in range(n):
    for j in range(1, m):
        prev = b[i][j - 1] - 1
        curr = b[i][j] - 1
        if curr - prev != 1 or prev // 7 != curr // 7:
            ok = False
            break

for i in range(m):
    for j in range(1, n):
        prev = b[j - 1][i]
        curr = b[j][i]
        if curr - prev != 7:
            ok = False
            break

print("Yes" if ok else "No")
