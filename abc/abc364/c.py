def solve(arr, z):
    arr.sort(reverse=True)
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > z:
            return i + 1
    return len(arr)


n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(min(solve(a, x), solve(b, y)))
