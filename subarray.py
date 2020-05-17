arr = [1, 2, 3, 4]
start = 0
while start < len(arr):
    end = start
    while end < len(arr):
        print(arr[start:end + 1])
        end += 1
    start += 1


