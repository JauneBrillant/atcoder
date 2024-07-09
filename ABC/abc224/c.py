n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]


def is_triangle(x1, x2, x3, y1, y2, y3):
    return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2 != 0


ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if is_triangle(
                xy[i][0],
                xy[j][0],
                xy[k][0],
                xy[i][1],
                xy[j][1],
                xy[k][1],
            ):
                ans += 1

print(ans)
