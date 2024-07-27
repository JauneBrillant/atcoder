h, w = map(int, input().split())
curr_i, curr_j = map(int, input().split())
curr_i -= 1
curr_j -= 1
grid = [list(input()) for _ in range(h)]
x = input()

for c in x:
    if c == "L" and curr_j > 0 and grid[curr_i][curr_j - 1] == ".":
        curr_j -= 1
    if c == "R" and curr_j < w - 1 and grid[curr_i][curr_j + 1] == ".":
        curr_j += 1
    if c == "U" and curr_i > 0 and grid[curr_i - 1][curr_j] == ".":
        curr_i -= 1
    if c == "D" and curr_i < h - 1 and grid[curr_i + 1][curr_j] == ".":
        curr_i += 1
    # print(curr_i, curr_j)

print(curr_i + 1, curr_j + 1)
