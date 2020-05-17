arr = [-2, -3, -2, -3, -5, -1]
mx = -10000000000
con_sum = 0
for i in range(len(arr)):
    con_sum += arr[i]
    if con_sum > mx:
        mx = con_sum

    if con_sum < 0:
        con_sum = 0
print(mx)
