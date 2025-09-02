class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def traverse_linked_list_recursive(a: Node):
    if a != None:
        print(a.val, end=" ")
        traverse_linked_list_recursive(a.next)
    return

def traverse_linked_list_itterative(a: Node):
    while a != None:
        print(a.val, end=" ")
        a = a.next
    

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

traverse_linked_list_recursive(a=a)

traverse_linked_list_itterative(a=a)