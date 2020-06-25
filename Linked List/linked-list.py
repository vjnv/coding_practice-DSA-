class Node:
    def __init__(self, v):
        self.data = v
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()
    return


def print_reverse(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next
    for i in reversed(range(len(stack))):
        print(stack[i], end=" ")
    print()
    return


def insert(head, value):
    new_node = Node(value)
    if head == None:
        head = new_node
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head


def middle_element(head):
    slow = head
    fast = head
    while fast.next and fast:
        fast = fast.next.next
        if fast == None:
            break
        slow = slow.next
    print(slow.data)
    return


list = linked_list()
list.head = insert(list.head, 1)
list.head = insert(list.head, 2)
list.head = insert(list.head, 3)
list.head = insert(list.head, 4)
list.head = insert(list.head, 5)
list.head = insert(list.head, 6)
print_list(list.head)
print_reverse(list.head)
middle_element(list.head)
