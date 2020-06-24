class Node:
    def __init__(self, v):
        self.data = v
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None


def print_reverse(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()
    return


def print_list(head):
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
    new_node.next = head
    head = new_node
    return head


list = linked_list()
list.head = insert(list.head, 1)
list.head = insert(list.head, 2)
list.head = insert(list.head, 3)
print_list(list.head)
print_reverse(list.head)
