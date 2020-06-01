def search(arr,l,r, k):
    mid = len(arr) // 2
    if len(arr)==1 and arr[0]!=k:
        return -1
    if arr[mid] == k:
        if arr[mid - 1] != k:
            return l+mid
        return search(arr[:mid],l,mid-1, k)
    if arr[mid] < k:
        return search(arr[mid + 1:],mid+1,r, k)
    if arr[mid] > k:
        return search(arr[:mid],l,mid-1, k)


arrs = [[[1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8],5],
        [[2,3,5,7,9,3],4]]
for arr in arrs:
    result=search(arr[0],0,len(arr),arr[1])
    print(result)