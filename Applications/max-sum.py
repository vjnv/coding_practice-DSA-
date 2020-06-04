# arr = [-2, 3, 2, -3, 5, 1]
arr = [-2, -3, -4, -1]
mx = -10000000000
con_sum = 0
start = end = t = 0
for i in range(len(arr)):
    con_sum += arr[i]
    if con_sum > mx:
        mx = con_sum
        start = t
        end = i
    if con_sum < 0:
        con_sum = 0
        t = i + 1
print(start, end)
print(mx)
