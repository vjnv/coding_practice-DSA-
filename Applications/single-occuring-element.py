def single_m2(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 3:
        if arr[0] != arr[1]:
            return arr[0]
        return arr[2]
    mid = len(arr) // 2
    if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
        return arr[mid]
    if arr[mid] == arr[mid - 1]:
        number_of_elements_in_left = mid + 1
        number_of_elements_in_right = len(arr) - mid
        if number_of_elements_in_left % 2 != 0:
            return single_m2(arr[:(mid + 1)])
        return single_m2(arr[(mid + 1):])
    if arr[mid] == arr[mid + 1]:
        number_of_elements_in_left = mid
        number_of_elements_in_right = len(arr) - mid + 1
        if number_of_elements_in_left % 2 != 0:
            return single_m2(arr[:mid])
        return single_m2(arr[mid:])


def single_m1(arr):
    if len(arr) == 1:
        return arr[0]
    i = 0
    while i < len(arr) - 1:
        if arr[i] != arr[i + 1]:
            return arr[i]
        i += 2
    return arr[len(arr) - 1]


# arr = [1, 1, 2, 3, 3, 4, 4, 5, 5]
# arr = [3, 3, 7, 7, 10, 11, 11, 12, 12]
# arr = [1, 2, 2, 4, 4, 5, 5, 6, 6]
# arr=[1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]
arr=[1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]

result1 = single_m1(arr)
result2 = single_m2(arr)
print(result1)
print(result2)
assert result1 == result2
