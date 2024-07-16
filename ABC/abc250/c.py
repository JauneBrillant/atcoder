n, q = map(int, input().split())

arr = [i for i in range(1, n + 1)]

hashmap = {}
for i in range(n):
    hashmap[i + 1] = i

for _ in range(q):
    l_num = int(input())
    l_pos = hashmap[l_num]

    if l_pos == n - 1:
        r_pos = n - 2
    else:
        r_pos = l_pos + 1
    r_num = arr[r_pos]

    arr[l_pos], arr[r_pos] = arr[r_pos], arr[l_pos]

    hashmap[l_num] = r_pos
    hashmap[r_num] = l_pos

print(*arr)
