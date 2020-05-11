n=12321
digits=[]
while n!=0:
    remainder=n%10
    n//=10
    digits.append(remainder)
print(digits)
ans=True
for i in range(len(digits)//2):
    if digits[i]!=digits[len(digits)-i-1]:
        ans=False
        break
if ans==True:
    print('Yes')
else:
    print('No')