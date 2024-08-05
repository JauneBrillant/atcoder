from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i, a in enumerate(A):
    ans = max(ans, bisect_left(A, a + M) - i)

print(ans)
