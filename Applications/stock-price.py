def profit_cal(arr):
    if len(arr)==0:
        return 0
    cost_price = arr[0]
    selling_price = arr[0]
    profit = 0
    for i in range(1, len(arr)):
        if arr[i] < cost_price:
            cost_price = arr[i]
            selling_price = arr[i]
        else:
            selling_price = arr[i]
        profit = max(profit, selling_price - cost_price)
    return profit


arrs = [[7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1]]
for arr in arrs:
    result = profit_cal(arr)
    print(result)
