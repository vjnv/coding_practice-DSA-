# r1=[1,2,4,5]
# r2=[3,3,6,6]
r1=[0,0,10,8]
r2=[2,3,7,9]
ans='Yes'
if r1[0]>r2[2]:
    ans='NO'
elif r1[2]<r2[0]:
    ans='NO'
elif r1[1]>r2[3]:
    ans='NO'
elif r1[3]<r2[1]:
    ans='NO'
print(ans)

