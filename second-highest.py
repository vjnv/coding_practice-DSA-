def sec_hig(arr):
    if len(arr) < 2:
        return "Invalid input"
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif max2 < arr[i] < max1:
            max2 = arr[i]
    return max2


# n = int(input("Enter the number of elements:"))
a = [10, 85, 45, 78, 55, 85]
print(sec_hig(a))
