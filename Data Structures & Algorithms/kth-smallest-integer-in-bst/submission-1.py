# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, cnt = root.val, k
        def dfs(root):
            nonlocal res, cnt
            if not root:
                return
            dfs(root.left)
            cnt -= 1
            if cnt == 0:
                res = root.val
            dfs(root.right)
            return

        dfs(root)
        return res