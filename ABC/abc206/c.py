n = int(input())

intervals = []
for _ in range(n):
    t, l, r = map(float, input().split())
    match t:
        case 1:
            intervals.append((l, r))
        case 2:
            intervals.append((l, r - 0.1))
        case 3:
            intervals.append((l - 0.1, r))
        case 4:
            intervals.append((l - 0.1, r - 0.1))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if intervals[i][r] >= intervals[j][l]:
            ans += 1

print(ans)
