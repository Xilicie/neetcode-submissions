class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            graph[crs].append(prq)
        
        visiting = set()
        visited = set()
        cycle = False
        res = []
        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
            visiting.add(crs)
            for prq in graph[crs]:
                if not dfs(prq):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res


            