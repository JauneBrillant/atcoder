n = int(input())
binary_str_n = format(n, "b")

one_digits = []
for i, c in enumerate(reversed(binary_str_n)):
    if c == "1":
        one_digits.append(i)
len = len(one_digits)

ans = []
for i in range(1 << len):
    num = 0
    for j in range(len):
        if i & (1 << j):
            num |= 1 << one_digits[j]
    ans.append(num)

ans.sort()
for e in ans:
    print(e)
