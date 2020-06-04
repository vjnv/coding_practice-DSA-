def reverse(arr):
    
    if len(arr) == 0:
        return "Empty array"
    if len(arr) == 1:
        return arr
    for i in range(0, len(arr) // 2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return arr

# arr = []
arr = [12, 11, 85, 78, 96, 45]
print(reverse(arr))
# print(arr)
