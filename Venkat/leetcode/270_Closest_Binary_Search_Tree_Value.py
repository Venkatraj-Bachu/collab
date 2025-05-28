# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        closest = root.val
        while root:
            if abs(root.val - target) < abs(target - closest):
                closest = root.val
            elif abs(root.val - target) == abs(target - closest):
                closest = min(root.val, closest)
            if root.val == target:
                return root.val

            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right

        return closest
