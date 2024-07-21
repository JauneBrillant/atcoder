s = input()
t = input()


def rle(s):
    res = []
    for c in s:
        if len(res) > 0 and res[-1][0] == c:
            res[-1][1] += 1
        else:
            res.append([c, 1])
    return res


def solve(s, t):
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i][0] != t[i][0]:
            return False

        if s[i][1] > t[i][1]:
            return False

        if s[i][1] == 1 and t[i][1] != 1:
            return False

    return True


ss = rle(s)
tt = rle(t)
print("Yes" if solve(ss, tt) else "No")
