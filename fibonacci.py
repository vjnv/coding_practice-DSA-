n = 7
a = [None] * n
if n == 1:
    a[0] = 1
    print(a)
elif n == 2:
    a[0], a[1] = 1, 1
    print(a)
else:
    a[0], a[1] = 1, 1
    for i in range(2, n):
        a[i] = a[i - 1] + a[i - 2]
    print(a)
