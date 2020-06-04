def partition(arr,l,r):
    i = l-1
    for j in range(l,r-1):
        if arr[j] < arr[r]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quick_sort(arr, l, r):
    if l < r:
        pi = partition(arr,l,r)
        quick_sort(arr, l, pi - 1)
        quick_sort(arr, pi + 1, r)


arr = [12, 45, 67, 34, 23, 87, 45]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
