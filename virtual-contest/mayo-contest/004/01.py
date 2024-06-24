n = int(input())
p = map(int, input().split())

min = 1e9
ans = 0
for e in p:
    if e <= min:
        min = e
        ans += 1

print(ans)
