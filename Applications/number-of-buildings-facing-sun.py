#sun is on LHS
def total_buildings(arr):
    count=1
    prev_building=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>prev_building:
            count+=1
            prev_building=arr[i]
    return count

# arr=[7,4,8,2,9]
# arr=[5,4,3,2,1]
arr=[5,4,3,2,1,6,7,8,9]
result=total_buildings(arr)
print(result)