n, t, p = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
while True:
    ans += 1
    cnt = 0
    for i in range(n):
        if arr[i] >= t:
            cnt += 1
        arr[i] += 1
    if cnt >= p:
        break

print(ans - 1)
