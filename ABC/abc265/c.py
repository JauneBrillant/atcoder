h, w = map(int, input().split())
g = [input() for _ in range(h)]

curr_i = 0
curr_j = 0
cnt = 0
while True:
    if cnt > h * w:
        print(-1)
        exit()
    cnt += 1

    if curr_i > 0 and g[curr_i][curr_j] == "U":
        curr_i -= 1
    elif curr_i + 1 < h and g[curr_i][curr_j] == "D":
        curr_i += 1
    elif curr_j > 0 and g[curr_i][curr_j] == "L":
        curr_j -= 1
    elif curr_j + 1 < w and g[curr_i][curr_j] == "R":
        curr_j += 1
    else:
        break


print(curr_i + 1, curr_j + 1)
