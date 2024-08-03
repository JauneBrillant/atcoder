n, x = map(int, input().split())
bags = []
for _ in range(n):
    bag = list(map(int, input().split()))
    bags.append(bag[1:])


def dfs(i, curr_product=1):
    if i == n:
        return 1 if curr_product == x else 0

    cnt = 0
    for num in bags[i]:
        cnt += dfs(i + 1, curr_product * num)

    return cnt


print(dfs(0))
