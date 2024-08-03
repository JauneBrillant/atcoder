r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

ans = 0
for bit in range(1 << r):
    curr_ans = 0
    for j in range(c):
        cnt = 0
        for i in range(r):
            if bit & (1 << i):
                cnt += 1 - grid[i][j]
            else:
                cnt += grid[i][j]
        curr_ans += max(cnt, r - cnt)
    ans = max(ans, curr_ans)

print(ans)
