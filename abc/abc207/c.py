from typing import List, Tuple

n = int(input())

intervals: List[Tuple[float, float]] = []


for _ in range(n):
    t, l, r = map(float, input().split())
    match t:
        case 1:
            intervals.append((l, r))
        case 2:
            intervals.append((l, r - 0.1))
        case 3:
            intervals.append((l + 0.1, r))
        case 4:
            intervals.append((l + 0.1, r - 0.1))

ans = n * (n - 1) // 2
for i in range(n):
    for j in range(i + 1, n):
        l, r = 0, 1
        if intervals[i][r] < intervals[j][l] or intervals[i][l] > intervals[j][r]:
            ans -= 1

print(ans)
