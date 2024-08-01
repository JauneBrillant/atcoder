n = int(input())
a = list(map(int, input().split()))

a = sorted(x - i - 1 for i, x in enumerate(a))
b = a[n // 2]
ans = sum(abs(x - b) for x in a)

print(ans)
