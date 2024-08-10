N = int(input())
A = list(map(int, input().split()))

ans = float("inf")
for bit in range(1 << N - 1):
    last_is_split = False
    orr = 0
    xor = 0
    for i in range(N - 1):
        orr |= A[i]
        if bit & 1 << i:
            xor ^= orr
            orr = 0
            if i == N - 2:
                last_is_split = True

    if last_is_split:
        xor ^= A[-1]
    else:
        orr |= A[-1]
        xor ^= orr

    ans = min(ans, xor)

print(ans)
