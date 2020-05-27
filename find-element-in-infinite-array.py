def binary_search(a, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            return binary_search(a, left, mid - 1, x)
        if a[mid] < x:
            return binary_search(a, mid + 1, right, x)
    return -1


def search(arr, element):
    start = 0
    end = 1
    temp = arr[0]
    while temp < element:
        start = end
        end *= 2
        temp = arr[end]

    return binary_search(arr, start, end, element)


arrs = [[3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170, 171, 172, 173, 174, 175, 176]]
for arr in arrs:
    element = int(input("Enter the element:"))
    res_index=search(arr, element)
    print(res_index)
