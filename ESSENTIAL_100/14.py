n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = float("inf")
for bit in range(1 << n):
    if bit.bit_count() != k or not bit & 1:
        continue

    selected = [False] * n
    for i in range(n):
        if bit & 1 << i:
            selected[i] = True

    cost = 0
    mx = a[0]
    for i in range(1, n):
        if selected[i]:
            if a[i] <= mx:
                cost += mx - a[i] + 1
                mx += 1
            else:
                mx = a[i]
    ans = min(ans, cost)

print(ans)
