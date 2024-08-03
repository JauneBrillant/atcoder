n = int(input())
a = list(map(int, input().split()))

cnt = sum(1 for i, x in enumerate(a) if x == i + 1)
ans = cnt * (cnt - 1) // 2

for i, num in enumerate(a):
    if i + 1 < num and a[num - 1] == i + 1:
        ans += 1

print(ans)
