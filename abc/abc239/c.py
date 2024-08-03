x1, y1, x2, y2 = map(int, input().split())

if x1 < 0:
    x2 += abs(x1)
else:
    x2 -= x1

if y1 < 0:
    y2 += abs(y1)
else:
    y2 -= y1

st = set()
p = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
for a, b in p:
    for c, d in p:
        st.add((a + c, b + d))

print("Yes" if (x2, y2) in st else "No")
