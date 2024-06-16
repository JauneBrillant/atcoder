n = int(input())

num = 0
for i in range(n):
    t, a = input().split()
    aa = int(a)

    match t:
        case "+":
            num += aa
        case "-":
            num -= aa
        case "*":
            num *= aa

    if num < 0:
        num += 10000

    num %= 10000
    print(num)
