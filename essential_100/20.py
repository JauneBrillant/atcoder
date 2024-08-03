from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()

ans = 0
for bi in b:
    pos_a = bisect_left(a, bi)
    pos_c = n - bisect_right(c, bi)
    ans += pos_a * pos_c

print(ans)
