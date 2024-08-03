m = int(input())
target = [tuple(map(int, input().split())) for _ in range(m)]
n = int(input())
stars = [tuple(map(int, input().split())) for _ in range(n)]
stars_st = set(stars)

x0, y0 = target[0]
for x, y in stars:
    dis_x = x - x0
    dis_y = y - y0

    for tx, ty in target:
        if (tx + dis_x, ty + dis_y) not in stars:
            ok = False
            break
    else:
        print(dis_x, dis_y)
