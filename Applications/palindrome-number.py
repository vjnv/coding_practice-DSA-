def palindrome_m1(n):
    digits = []
    while n != 0:
        remainder = n % 10
        n //= 10
        digits.append(remainder)
    print(digits)
    ans = True
    for i in range(len(digits) // 2):
        if digits[i] != digits[len(digits) - i - 1]:
            ans = False
            break
    if ans == True:
        print('Yes')
    else:
        print('No')


def palindrome_m2(n):
    rev = 0
    tmp = n
    while n != 0:
        r = n % 10
        n //= 10
        rev = rev * 10 + r
    print(rev)
    if tmp == rev:
        print('Yes')
    else:
        print('No')


n = 12321
palindrome_m1(n)
palindrome_m2(n)
