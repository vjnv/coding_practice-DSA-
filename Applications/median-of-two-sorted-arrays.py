def med(arr1,arr2):
    arr3=[]
    i=j=k=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
        k+=1
    while i<len(arr1):
        arr3.append(arr1[i])
        i+=1
        k+=1
    while j<len(arr2):
        arr3.append(arr2[j])
        j+=1
        k+=1
    n=len(arr3)
    m=n//2
    if n%2!=0:
        return arr3[m]
    else:
        return (arr3[m]+arr3[m-1])/2

arr1=[1,12,15,26,38]
arr2=[2,13,17,30,45]
median=med(arr1,arr2)
print(median)
