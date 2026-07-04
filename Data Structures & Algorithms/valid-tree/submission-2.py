class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is acyclic, connected, undirected graph
        if len(edges) != n - 1:
            return False

        graph = {i : [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()
        def dfs(n):
            if n in visited:
                return False
            visited.add(n)

            for nbr in graph[n]:
                if nbr == n:    
                    continue
                dfs(nbr)
            return True


        return dfs(0) and len(visited) == n
        