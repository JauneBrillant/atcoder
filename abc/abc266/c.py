# 凸四角形とは
# すべての内角が180度未満である四角形(へこんでいない四角形)

# 凸四角形であるかの判定
# すべての内角が180度未満であれば良い

# 四角形のすべての頂点において、次の頂点への方向が反時計回りであることを確認することで判定
# ベクトルの外積を用いて角度の方向を確認 >> 反時計回りの場合、外積は正の値を持つ

a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))
d = tuple(map(int, input().split()))


def is_convex_quadrilateral(a, b, c, d):
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    return (
        cross_product(a, b, c) > 0
        and cross_product(b, c, d) > 0
        and cross_product(c, d, a) > 0
        and cross_product(d, a, b) > 0
    )


print("Yes" if is_convex_quadrilateral(a, b, c, d) else "No")
