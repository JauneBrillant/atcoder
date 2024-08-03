s = input()


def is_ok(passwd):
    for i, c in enumerate(s):
        if c == "o" and str(i) not in passwd:
            return False
        if c == "x" and str(i) in passwd:
            return False
    return True


ans = 0
for passwd in range(10000):
    if is_ok(str(passwd).zfill(4)):
        ans += 1

print(ans)
