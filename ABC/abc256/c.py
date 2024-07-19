h1, h2, h3, w1, w2, w3 = map(int, input().split())

# a b c
# d e f
# g h i

ans = 0
for a in range(1, 29):
    for b in range(1, 29):
        for d in range(1, 29):
            for e in range(1, 29):
                c = h1 - a - b
                f = h2 - d - e
                g = w1 - d - a
                h = w2 - e - b

                if c > 0 and f > 0 and g > 0 and h > 0:
                    i = w3 - c - f
                    if i == h3 - g - h and i > 0:
                        ans += 1

print(ans)
