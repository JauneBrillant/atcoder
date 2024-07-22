import copy

h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]

h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]

diff_h = h1 - h2
diff_w = w1 - w2


def del_rows():
    res = []
    for bit in range(1 << h1):
        if sum(1 for c in bin(bit) if c == "1") != diff_h:
            continue

        after_arr = []
        for i in range(h1):
            if not bit & 1 << i:
                after_arr.append(a[i])
        res.append(after_arr)
    return res


def del_cols(grids):
    for grid in grids:
        for bi in range(1 << w1):
            if sum(1 for c in bin(bi) if c == "1") != diff_w:
                continue

            cp_grid = copy.deepcopy(grid)
            for i in range(w1 - 1, -1, -1):
                if bi & (1 << i):
                    for j in range(h2):
                        cp_grid[j].pop(i)

            if cp_grid == b:
                return True
    return False


poss_rows = del_rows()
poss = del_cols(poss_rows)
print("Yes" if del_cols(poss_rows) else "No")
