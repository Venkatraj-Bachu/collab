# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        head = root
        while root:
            if root.val > val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    return head
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return head