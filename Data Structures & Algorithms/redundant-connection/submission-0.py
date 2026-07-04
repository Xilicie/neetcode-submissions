class Solution:
    def find(self, x, parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)
        return parent[x]
    
    def union(self, x, y, parent):
        rootX = self.find(x, parent)
        rootY = self.find(y, parent)
        if rootX == rootY:
            return False
        parent[rootY] = rootX
        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        for u, v in edges:
            if not self.union(u, v, parent):
                return [u, v]
