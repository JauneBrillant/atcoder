n = int(input())


def f(x):
    if x == 1:
        return "1"
    else:
        return f(x - 1) + " " + str(x) + " " + f(x - 1)


ans = f(n)
print(ans)
