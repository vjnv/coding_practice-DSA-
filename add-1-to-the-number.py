def add1(n):
    for i in reversed(range(len(n))):
        if n[i]==9:
            n[i]=0
        else:
            n[i]+=1
            break
    if n[0]==0:
        n.insert(0,1)
    print(n)

ns=[[1,2,9],
    [9,9,9],
    [2,3,4,9,9,9],
    [9,5,4,9,9]]
for n in ns:
    add1(n)