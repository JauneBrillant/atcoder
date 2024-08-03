from bisect import bisect_left

n = int(input())
s = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
s.sort()

ans = 0
for num in t:
    pos = bisect_left(s, num)
    if 0 <= pos < n and num == s[pos]:
        ans += 1

print(ans)
