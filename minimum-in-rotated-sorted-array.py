arr = [3,4,5,1,2]
if len(arr) == 0:
    print("Invalid input!!")
else:
    ans = 0
    for i in range(1, len(arr) - 1):
        if arr[i + 1] < arr[i]:
            ans = i + 1
            break
    print(arr[ans])
