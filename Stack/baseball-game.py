def total_score(arr):
    stack=[]
    score=0
    for i in range(len(arr)):
        l = len(stack)
        if arr[i]=="+":
            if l>=2:
                score+=stack[l-1]+stack[l-2]
                stack.append(stack[l-1]+stack[l-2])
            else:
                return "invalid expression"
        elif arr[i]=="D":
            if l>=1:
                score+=2*stack[l-1]
                stack.append(2*stack[l-1])
            else:
                return "invalid expression"
        elif arr[i]=="C":
            if l>=1:
                score-=stack[l-1]
                stack.pop()
            else:
                return "invalid expression"
        else:
            temp=int(arr[i])
            score+=temp
            stack.append(temp)
    print("stack:",stack,end=" ")
    return score


arrs=[["10", "5", "2", 'C', 'D', '+'],
      ["10", "20", 'D', 'D', 'D', '+'],
      ["10", "20", 'D', 'D', 'D', '+', 'C', 'C'],
      ["10", "20", 'C', 'D', 'C', '+', 'D', "10"],
      ["5", "2", "C", "D", "+"],
      ["5", "10", "20", 'C', 'D', 'C', '+', 'D', "10"]]
for arr in arrs:
    score=total_score(arr)
    print("score:",score)