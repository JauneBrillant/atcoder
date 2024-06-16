s = input()

ness = set()
not_ness = set()
for i, c in enumerate(s):
    match c:
        case "o":
            ness.add(i)
        case "x":
            not_ness.add(i)
        case "?":
            pass

ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                ok = True
                st = {i, j, k, l}

                for e in ness:
                    if e not in st:
                        ok = False

                for e in not_ness:
                    if e in st:
                        ok = False

                if ok:
                    ans += 1

print(ans)
