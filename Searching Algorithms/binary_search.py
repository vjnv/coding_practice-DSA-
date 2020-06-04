def binary(a, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            return binary(a, left, mid - 1, x)
        if a[mid] < x:
            return binary(a, mid + 1, right, x)
    return -1



arr = [10, 14, 19, 27, 33, 35, 42]
x = int(input("Enter the value of x:"))
# print(x)
res = binary(arr, 0, len(arr) - 1, x)
print(res)
