class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:   return n
        graph = {i : [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        res = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node) 
            for neighbor in graph[node]:
                dfs(neighbor)     
        
        for node in graph:
            if node not in visited:
                dfs(node)
                res += 1
        return res