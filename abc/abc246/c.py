n, k, x = map(int, input().split())
a = list(map(int, input().split()))

pays = []
for ai in a:
    if k <= 0 or ai < x:
        pays.append(ai)
    else:
        if ai // x <= k:
            pays.append(ai % x)
            k -= ai // x
        else:
            while k > 0 and ai - x >= 0:
                ai -= x
                k -= 1
            pays.append(ai)

ans = sum(pays)

pays.sort(reverse=True)
i = 0
while k > 0 and i < n:
    ans -= pays[i]
    i += 1
    k -= 1

print(ans)
