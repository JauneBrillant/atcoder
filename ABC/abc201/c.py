s = input()

ans = 0
for i in range(10000):
    ok = True
    passwd = str(i).zfill(4)
    for j, c in enumerate(s):
        if c == "o":
            if str(j) not in passwd:
                ok = False
                break
        if c == "x":
            if str(j) in passwd:
                ok = False
                break
    if ok:
        ans += 1

print(ans)
