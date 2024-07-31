h, w = map(int, input().split())
n = min(h, w)
c = [list(input()) for _ in range(h)]


def is_cross_size_t(i, j, t):
    if c[i][j] != "#":
        return False

    if (
        i - t >= 0
        and i + t < h
        and j - t >= 0
        and j + t < w
        and c[i - t][j - t] == "#"
        and c[i - t][j + t] == "#"
        and c[i + t][j - t] == "#"
        and c[i + t][j + t] == "#"
    ):
        return True
    return False


ans = [0] * (n + 1)
for i in range(h):
    for j in range(w):
        t = 1
        while is_cross_size_t(i, j, t):
            t += 1
        ans[t - 1] += 1

print(*ans[1:])
