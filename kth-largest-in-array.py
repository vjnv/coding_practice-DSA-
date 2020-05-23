def partition(arr, l, r):
    i = l - 1
    for j in range(l, r):
        if arr[j] < arr[r]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def k_largest(arr, left, right, l_k):
    if left <= right:
        pivot = partition(arr, left, right)
        if pivot < l_k:
            return k_largest(arr, pivot + 1, right, l_k)
        if pivot > l_k:
            return k_largest(arr, left, pivot - 1, l_k)
        return arr[pivot]


arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
ans = k_largest(arr, 0, len(arr) - 1, len(arr) - k)
print(ans)
