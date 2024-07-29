n = int(input())
a = list(map(int, input().split()))
a = set(a)

ans = 0
cost = 0
current_vol = 1
while cost < n:
    if current_vol in a:
        cost += 1
    else:
        cost += 2

    if cost <= n:
        ans = current_vol
        current_vol += 1

print(ans)
