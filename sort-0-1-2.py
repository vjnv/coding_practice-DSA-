# program to sort array containing 0s and 1s using only left
arr1=[0,1,0,0,0,0,1,1,0]
i=-1
for j in range(len(arr1)):
    if arr1[j]==0:
        i+=1
        arr1[i],arr1[j]=arr1[j],arr1[i]
print(arr1)



#program for sorting the array containing 0s and 1s using left right
arr = [0, 1, 0, 1, 1, 0, 1, 1, 0]
left = 0
right = len(arr) - 1
while left < right:
    while arr[left] == 0:
        left += 1
    while arr[right] == 1:
        right -= 1
    if left < right:
        arr[left] = 0
        arr[right] = 1
        left += 1
        right -= 1
print(arr)



#program to sort array containing 0s,1s and 2s
arr = [0, 1, 2, 2, 0, 0, 1, 1, 1, 0, 0]
left = 0
right = len(arr)-1
mid=0
while mid<right:
    if arr[mid]==0:
        arr[mid],arr[left]=arr[left],arr[mid]
        mid+=1
        left+=1
    elif arr[mid]==1:
        mid+=1
    else:
        arr[mid],arr[right]=arr[right],arr[mid]
        right-=1
print(arr)