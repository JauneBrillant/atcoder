from sortedcontainers import SortedList

st = SortedList()
ans = []

n = int(input())
for _ in range(n):
    query = input().split()
    type = int(query[0])

    match type:
        case 1:
            st.add(int(query[1]))
        case 2:
            tar = int(query[1])
            t = int(query[2])
            t = min(t, st.count(tar))
            while t > 0:
                st.discard(tar)
                t -= 1
        case 3:
            ans.append(st[-1] - st[0])

print(*ans)
