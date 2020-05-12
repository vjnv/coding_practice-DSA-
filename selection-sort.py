def selection_sort(arr):
    for i in range(len(arr)):
        max=0
        for j in range(len(arr)-i):
            if arr[j]>arr[max]:
                max=j
        arr[len(arr)-i-1],arr[max]=arr[max],arr[len(arr)-i-1]
arr=[1,2,32,23,12,15,26,34,27]
selection_sort(arr)
print(arr)