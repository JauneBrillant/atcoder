# 公差がマイナスの場合は反対に並び替える
# 初項が2, 公差が-3, 項数が４ >> 初項を-7, 公差を+3, 項数は変わらず4
# 2 -1 -4 -7 >> -7 -4 -1 2


x, a, d, n = map(int, input().split())

if d == 0:
    print(abs(a - x))
    exit()

if d < 0:
    a = a + d * (n - 1)
    d = -d

# xより小さい数値の最大値のインデックスiを求める
i = (x - a) // d
print(i)


def f(i):
    if i < 0:
        i = 0
    if i >= n:
        i = n - 1
    return a + d * i


ans = min(abs(f(i) - x), abs(f(i + 1) - x))
print(ans)
