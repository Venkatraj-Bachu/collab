# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pr(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    def su(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.su(root)
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                root.val = self.pr(root)
                root.left = self.deleteNode(root.left, root.val)
            
        return root
                
        