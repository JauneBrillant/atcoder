ss = [input() for _ in range(9)]


def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)


ans = set()
for ai in range(9):
    for aj in range(9):
        for bi in range(9):
            for bj in range(9):
                for ci in range(9):
                    for cj in range(9):
                        for di in range(9):
                            for dj in range(9):
                                if (
                                    ss[ai][aj]
                                    == ss[bi][bj]
                                    == ss[ci][cj]
                                    == ss[di][dj]
                                    == "#"
                                ) and ((ai, aj) != (bi, bj) != (ci, cj) != (di, dj)):
                                    ab = get_distance(ai, aj, bi, bj)
                                    bc = get_distance(bi, bj, ci, cj)
                                    cd = get_distance(ci, cj, di, dj)
                                    da = get_distance(di, dj, ai, aj)
                                    ac = get_distance(ai, aj, ci, cj)
                                    bd = get_distance(bi, bj, di, dj)
                                    if (
                                        ab == bc == cd == da
                                        and ac == bd
                                        and ac == ab + bc
                                    ):
                                        item = tuple(
                                            sorted(
                                                [(ai, aj), (bi, bj), (ci, cj), (di, dj)]
                                            )
                                        )
                                        ans.add(item)
print(len(ans))
