from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for _ in range(Q):
    b, k = map(int, input().split())
    left, right = -1, 10**9
    while left + 1 < right:
        mid = (left + right) // 2
        cnt = bisect_right(A, b + mid) - bisect_left(A, b - mid)
        if cnt >= k:
            right = mid
        else:
            left = mid
    print(right)
