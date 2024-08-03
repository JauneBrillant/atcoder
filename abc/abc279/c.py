h, w = map(int, input().split())
s = [input() for _ in range(h)]
t = [input() for _ in range(h)]


def solve(s, t):
    s_cols = list(map(list, zip(*s)))
    t_cols = list(map(list, zip(*t)))
    # s_cols = ["".join(s[i][j] for i in range(h)) for j in range(w)]
    # t_cols = ["".join(t[i][j] for i in range(h)) for j in range(w)]
    return sorted(s_cols) == sorted(t_cols)


print("Yes" if solve(s, t) else "No")
