n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

for i in range(p, q + 1):
    for j in range(r, s + 1):
        if i + j == a + b or i - j == a - b:
            print("#", end="")
        else:
            print(".", end="")
    print("")
