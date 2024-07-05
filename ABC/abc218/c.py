n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]


def normalize(a):
    min_i, min_j = n, n
    for i in range(n):
        for j in range(n):
            if a[i][j] == "#":
                min_i = min(min_i, i)
                min_j = min(min_j, j)
    res = [["."] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == "#":
                res[i - min_i][j - min_j] = "#"
    return res


def same(s, t):
    return normalize(s) == normalize(t)


def rotate(a):
    res = [["."] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n - 1 - i] = a[i][j]
    return res


ok = False
for _ in range(4):
    if same(s, t):
        ok = True
        break
    t = rotate(t)

print("Yes" if ok else "No")
