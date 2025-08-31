class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_linked_list_vals(head: Node):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

linked_list_vals = get_linked_list_vals(head=a)
print(linked_list_vals)
