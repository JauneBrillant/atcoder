n, x, y = map(int, input().split())


def red(n):
    if n < 2:
        return 0
    return red(n - 1) + blue(n) * x


def blue(n):
    if n < 2:
        return 1
    return red(n - 1) + blue(n - 1) * y


print(red(n))
