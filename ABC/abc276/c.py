def prev_permutation(arr):
    if arr == sorted(arr):
        return None

    i = len(arr) - 2
    while i >= 0 and arr[i] < arr[i + 1]:
        i -= 1

    j = len(arr) - 1
    while arr[j] >= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1 :] = reversed(arr[i + 1 :])
    return arr


n = int(input())
p = list(map(int, input().split()))
print(*prev_permutation(p))
