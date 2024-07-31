h1, h2, h3, w1, w2, w3 = map(int, input().split())

# a | b | c
# d | e | f
# g | h | i

ans = 0
for a in range(1, 31):
    for b in range(1, 31):
        for d in range(1, 31):
            for e in range(1, 31):
                g = h1 - a - d
                h = h2 - b - e
                c = w1 - a - b
                f = w2 - d - e
                i = w3 - g - h
                if g < 1 or h < 1 or c < 1 or f < 1 or i < 1:
                    continue
                if c + f + i == h3:
                    ans += 1

print(ans)
