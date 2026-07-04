# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balance = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(root):
            if not root:
                return 0
            left = h(root.left)
            right = h(root.right)
            if abs(left - right) > 1:
                self.balance = False
            return max(left, right) + 1
        h(root)
        return self.balance