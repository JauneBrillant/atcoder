import bisect

n = int(input())
s = input()
w = list(map(int, input().split()))

ad = []
ch = []
for i in range(n):
    if s[i] == "0":
        ch.append(w[i])
    else:
        ad.append(w[i])
ad.sort()
ch.sort()

ans = max(len(ad), len(ch))
ad_len = len(ad)
for i, x in enumerate(ch):
    idx = bisect.bisect_right(ad, x)
    ad_numbers = ad_len - idx
    ch_numbers = i + 1
    ans = max(ans, ad_numbers + ch_numbers)

print(ans)
