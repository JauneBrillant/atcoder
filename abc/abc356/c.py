n, m, k = map(int, input().split())
tests = [input().split()[1:] for _ in range(m)]

ans = 0
for bit in range(1 << n):
    for *keys, res in tests:
        right_key_cnt = sum(1 for key in keys if bit & 1 << int(key) - 1)
        if (res == "o" and right_key_cnt < k) or res == "x" and right_key_cnt >= k:
            break
    else:
        ans += 1
print(ans)
