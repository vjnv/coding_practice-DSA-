def water_trapped(arr):
    water_trapped = 0
    left_max = [None] * len(arr)
    left_max[0] = arr[0]
    for i in range(1, len(left_max)):
        left_max[i] = max(left_max[i - 1], arr[i])
    right_max = [None] * len(arr)
    right_max[len(arr) - 1] = arr[len(arr) - 1]
    for i in reversed(range(len(left_max) - 1)):
        right_max[i] = max(arr[i], right_max[i + 1])
    for i in range(len(arr)):
        water_on_the_building = min(left_max[i], right_max[i])
        w_i = water_on_the_building - arr[i]
        water_trapped += w_i
    return water_trapped


arrs = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [0, 0, 0, 0],
        [1, 3, 5, 7, 9, 11, 13],
        [20, 18, 16, 12, 8, 6, 4, 2, 1]]
for arr in arrs:
    result = water_trapped(arr)
    print(result)
