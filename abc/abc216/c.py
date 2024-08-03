n = int(input())

ans = ""
while n > 0:
    if n & 1:
        n -= 1
        ans = "A" + ans
    else:
        n //= 2
        ans = "B" + ans

print(ans)
