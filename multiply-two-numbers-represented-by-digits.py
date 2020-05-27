# function two add two arrays
def add_arrs(arr1, arr2):
    # adding leading zeroes to make the length of both array equal
    if len(arr1) < len(arr2):
        while len(arr2) != len(arr1):
            arr1.insert(0, 0)
    else:
        while len(arr2) != len(arr1):
            arr2.insert(0, 0)
    carry = 0
    result = [None] * len(arr1)
    # adding index by index and maintaining carry
    for i in reversed(range(len(arr1))):
        result[i] = arr1[i] + arr2[i] + carry
        carry = result[i] // 10
        result[i] %= 10
    if carry != 0:
        result.insert(0, carry)
    return result

# function to multiply arrays
def multiply_arrs(arr1, arr2):
    # adding leading zeroes to make th length of both arrays equal
    if len(arr1) < len(arr2):
        while len(arr2) != len(arr1):
            arr1.insert(0, 0)
    else:
        while len(arr2) != len(arr1):
            arr2.insert(0, 0)
    result=[0]*(len(arr1)+len(arr2))
    # multiplying arrays
    for i in reversed(range(len(arr2))):
        # temporary array to store the value of resultant by multiplying one digit of arr2 to arr1
        temp=[0]*(len(arr1))
        carry=0
        for j in reversed(range(len(arr1))):
            temp[j]=arr1[j]*arr2[i] + carry
            carry=temp[j]//10
            temp[j]%=10
        # adding the carry to the startng of array
        if carry!=0:
            temp.insert(0,carry)
        # appending zeroes at the end of temp as we move from one place to tens then multiply by 10 and so on.....
        for j in range(len(arr2)-i-1):
            temp.append(0)
        result=add_arrs(result,temp)
    while result[0]==0:
        result=result[1:]
    return result
numbers=[[[1],[9]],
         [[1,3],[3,6,7]],
         [[1,2,3],[9,1]],
         [[3,5,7,4],[5,0,0,6,5]]]
for nos in numbers:
    result=multiply_arrs(nos[0],nos[1])
    print(result)