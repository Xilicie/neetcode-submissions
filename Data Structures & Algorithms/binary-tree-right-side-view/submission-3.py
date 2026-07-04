# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            lenq = len(q)
            r = None
            for _ in range(lenq):
                node = q.popleft()
                if node:
                    r = node.val
                    q.append(node.left)
                    q.append(node.right)
            if r is not None:
                res.append(r)
        return res