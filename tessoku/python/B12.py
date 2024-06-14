n = int(input())

l = 0.0
r = 100.0

for i in range(20):
    m = (l + r) / 2
    if m**3 + m <= n:
        l = m
    else:
        r = m

print(m)
