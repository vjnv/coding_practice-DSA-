# number is represented as reversed list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1, l2):
    carry = 0
    n1 = l1.val
    n2 = l2.val
    addn = n1 + n2
    if addn > 9:
        carry = 1
        addn = addn % 10
    res = ListNode(addn)
    head = res
    l1 = l1.next
    l2 = l2.next
    while l1 and l2:
        n1 = l1.val
        n2 = l2.val
        addn = n1 + n2
        if carry:
            addn = addn + carry
            carry = 0
        if addn > 9:
            carry = 1
            addn = addn % 10
        res.next = ListNode(addn)
        res = res.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        addn = l1.val
        if carry:
            addn = addn + carry
            carry = 0
        if addn > 9:
            carry = 1
            addn = addn % 10
        res.next = ListNode(addn)
        res = res.next
        l1 = l1.next
    while l2:
        addn = l2.val
        if carry:
            addn = addn + carry
            carry = 0
        if addn > 9:
            carry = 1
            addn = addn % 10
        res.next = ListNode(addn)
        res = res.next
        l2 = l2.next
    if carry:
        res.next = ListNode(carry)
    res = res.next
    return head


def insert(root, item):
    temp = ListNode(item)

    if root == None:
        root = temp
    else:
        ptr = root
        while ptr.next:
            ptr = ptr.next
        ptr.next = temp

    return root


def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])

    return root


def display(root):
    while root:
        print(root.val, end=" ")
        root = root.next


arr1 = [2, 4, 3]
arr2 = [5, 6, 4]
l1 = arrayToList(arr1, len(arr1))
l2 = arrayToList(arr2, len(arr2))
res = addTwoNumbers(l1, l2)
display(res)
