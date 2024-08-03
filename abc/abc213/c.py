h, w, n = map(int, input().split())
rows, cols = [], []

for i in range(n):
    a, b = map(int, input().split())
    rows.append(a)
    cols.append(b)

d = {v: i + 1 for i, v in enumerate(sorted(list(set(rows))))}
e = {v: i + 1 for i, v in enumerate(sorted(list(set(cols))))}

for i, j in zip(rows, cols):
    print(d[i], e[j])
