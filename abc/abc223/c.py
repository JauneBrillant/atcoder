n = int(input())
a = []
b = []

t = 0.0
for _ in range(n):
    ai, bi = map(int, input().split())
    t += ai / bi
    a.append(ai)
    b.append(bi)

t /= 2
ans = 0.0
for i in range(n):
    ans += min(a[i], t * b[i])
    t -= min(a[i] / b[i], t)

print(ans)
