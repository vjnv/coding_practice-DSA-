def look_and_say(n):
    if n==1:
        return "1"
    if n==2:
        return "11"
    prev="11"
    for i in range(3,n+1):
        count=1
        res = ""
        for j in range(1,len(prev)):
            if prev[j]!=prev[j-1]:
                res=res+str(count)+prev[j-1]
                count=1
            else:
                count+=1
        res=res+str(count)+prev[len(prev)-1]
        prev=res
    return prev
for n in range(1,10):
    result=look_and_say(n)
    print(result)