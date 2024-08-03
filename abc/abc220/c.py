n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum_a = sum(a)
ans = (x // sum_a) * n
total = sum_a * (x // sum_a)

i = 0
while total <= x:
    total += a[i]
    ans += 1
    i += 1

print(ans)
