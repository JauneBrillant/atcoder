n = int(input())
a = []
b = []
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
    ans += abs(x - y)
a.sort()
b.sort()

start = a[len(a) // 2]
end = b[len(b) // 2]

for i in range(n):
    ans += abs(a[i] - start)
    ans += abs(b[i] - end)

print(ans)
