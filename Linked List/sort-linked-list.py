class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


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


def mergeTwoLists(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val > l2.val:
        l1, l2 = l2, l1
    head1 = l1
    head2 = l2
    prev = head1
    while head1 and head2:
        while head1.next and head1.next.val < head2.val:
            prev = head1
            head1 = head1.next
        if head1.next:
            temp_next1 = head1.next
            head1.next = head2
            head2 = head2.next
            head1.next.next = temp_next1
            prev = head1
            head1 = head1.next
        else:
            head1.next = head2
            head2 = None
            break
    if head2:
        prev.next = head2
    return l1


def mergesort(ll):
    if ll is None:
        return ll
    if ll.next is None:
        return ll
    slow = ll
    fast = ll
    while fast.next and fast:
        fast = fast.next.next
        if fast is None:
            break
        slow = slow.next
    list1 = ll
    list2 = slow.next
    slow.next = None
    list1 = mergesort(list1)
    list2 = mergesort(list2)
    return mergeTwoLists(list1, list2)


arrs = [[2, 7, 8, 9, 6, 3, 4],
        [15, 10, 5, 3, 2, 4, 5, 1]]
for arr1 in arrs:
    l1 = arrayToList(arr1, len(arr1))
    # l2 = arrayToList(arr2, len(arr2))
    res = mergesort(l1)
    display(res)
    print()
