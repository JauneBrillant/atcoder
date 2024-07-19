n, q = map(int, input().split())
s = input()

cnt = 0
for _ in range(q):
    type, x = map(int, input().split())
    match type:
        case 1:
            cnt += x
        case 2:
            print(s[(x - 1 - cnt) % n])
