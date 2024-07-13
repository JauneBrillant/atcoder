x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


ab = (x1 - x2) ** 2 + (y2 - y1) ** 2
bc = (x2 - x3) ** 2 + (y2 - y3) ** 2
ca = (x3 - x1) ** 2 + (y3 - y1) ** 2

if ab == bc + ca or bc == ab + ca or ca == ab + bc:
    print("Yes")
else:
    print("No")
