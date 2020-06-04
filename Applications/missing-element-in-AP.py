def find(arr, l, r, d):
    mid = l + (r - l) // 2
    tmp = arr[0] + (mid) * d
    if l < r:
        if tmp < arr[mid]:
            return find(arr, l, mid, d)
        if tmp == arr[mid]:
            return find(arr, mid + 1, r, d)
    if l == r:
        return tmp


arrs = [[2, 4, 6, 8, 10, 14, 16, 18],
        [2, 6, 8, 10],
        [1, 4, 7, 13, 16],
        [8, 5, 2, -4],
        [-10, 0, 20, 30, 40],
        [-5, -10, -15, -25],
        [-12, -7, -2, 8, 13],
        [20, 14, 8, 2, -10]]
for arr in arrs:
    d = (arr[len(arr) - 1] - arr[0]) / (len(arr))
    res = find(arr, 0, len(arr) - 1, d)
    print(res)
