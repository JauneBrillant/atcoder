mod = 998244353


def calc(i):
    n = 10**i - 10 ** (i - 1)
    start = 1
    end = n
    return n * (start + end) // 2


s = input()
ans = 0
for i in range(1, len(s)):
    ans += calc(i)
    ans %= mod

len = len(s)
start = 10 ** (len - 1)
end = int(s)
kou = end - start + 1
ans += kou * (1 + kou) // 2
ans %= mod
print(ans)
