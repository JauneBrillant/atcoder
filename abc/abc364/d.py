from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


# A の中で点B との距離がk番目のもの = 点B からある範囲を指定した時に、その範囲内の点がk個以上であるものの最小値
# 点B から範囲を二分探索し、その範囲内で点がk個以上で
# --- NG | OK ---


# 範囲内に点がk個以上あるか？
def cond(b, m, k):
    return bisect_right(A, b + m) - bisect_left(A, b - m) >= k


for _ in range(Q):
    b, k = map(int, input().split())

    ng, ok = -1, 10**9
    while ng + 1 < ok:
        mid = (ng + ok) // 2
        if cond(b, mid, k):
            ok = mid
        else:
            ng = mid
    print(ok)
