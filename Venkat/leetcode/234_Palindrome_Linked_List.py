# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
                      
        # '''
        # Maintain a stack. Push values of the linked list to the stack while traversing. Next traverse again while popping elements from the stack. 
        # Time: O(N)
        # Space: O(N)
        # '''

        # stack = []
        # temp = head
        # while temp:
        #     stack.append(temp.val)
        #     temp = temp.next
        
        # while head:
        #     if stack.pop() != head.val:
        #         return False
        #     head = head.next
        
        # return True

        '''
        Reverse second half of the linked list in place and then compare it with 1st half.
        Time: O(N)
        Space: O(1)
        '''

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, cur = None, slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        reverse_second_half = prev
        res = True
        while head and reverse_second_half:
            if head.val != reverse_second_half.val:
                res = False
                break
            head = head.next
            reverse_second_half = reverse_second_half.next

        # prev, cur = None, reverse_second_half
        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nxt
        
        return res