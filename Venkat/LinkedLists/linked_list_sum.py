class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_sum(head: Node):
    cur_sum = 0
    while head:
        cur_sum += head.val
        head = head.next
    
    return cur_sum

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print(linked_list_sum(a))