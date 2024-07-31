n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(m)]


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


for a, b in ab:
    close_j = min(range(m), key=lambda j: get_distance(a, b, *cd[j]))
    print(close_j + 1)
