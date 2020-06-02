def spiral(arr):
    left=0
    right=len(arr[0])
    top=0
    bottom=len(arr)
    ans=[]
    while left<right and top<bottom:
        for i in range(left,right):
            print(arr[top][i],end=" ")
            ans.append(arr[top][i])
        top+=1
        for i in range(top,bottom):
            print(arr[i][right-1],end=" ")
            ans.append(arr[i][right-1])
        right-=1
        if top<bottom:
            for i in reversed(range(left,right)):
                print(arr[bottom-1][i],end=" ")
                ans.append(arr[bottom-1][i])
        bottom-=1
        if left<right:
            for i in reversed(range(top,bottom)):
                print(arr[i][left],end=" ")
                ans.append(arr[i][left])
        left+=1


arrs=[[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
      [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]]

for arr in arrs:
    spiral(arr)
    print()