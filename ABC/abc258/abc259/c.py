def rle(st):
    res = []
    for c in st:
        if len(res) > 0 and c == res[-1][0]:
            res[-1][1] += 1
        else:
            res.append([c, 1])
    return res


def solve(a, b):
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        char_a, cnt_a = a[i]
        char_b, cnt_b = b[i]

        if char_a != char_b:
            return False

        if cnt_a == 1 and cnt_b > 1:
            return False

        if cnt_a > cnt_b:
            return False

    return True


s = input()
t = input()

a = rle(s)
b = rle(t)
print("Yes" if solve(a, b) else "No")
