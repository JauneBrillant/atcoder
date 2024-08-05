n, m, k = map(int, input().split())
tests = [[] for _ in range(m)]
results = []
for i in range(m):
    test = input().split()
    c = int(test[0])
    for j in range(c):
        tests[i].append(test[1 + j])
    results.append(test[-1])

ans = 0
for bit in range(1 << n):
    selected_right_key = set()
    for i in range(n):
        if bit & 1 << i:
            selected_right_key.add(i + 1)

    ok = True
    for i, test in enumerate(tests):
        right_key_cnt = sum(1 for key in test if int(key) in selected_right_key)

        if results[i] == "o" and right_key_cnt < k:
            ok = False
            break
        if results[i] == "x" and right_key_cnt >= k:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
