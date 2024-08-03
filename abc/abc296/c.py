n, x = map(int, input().split())
a = list(map(int, input().split()))
st = set(a)

for ai in a:
    if ai - x in st:
        exit(print("Yes"))

print("No")
