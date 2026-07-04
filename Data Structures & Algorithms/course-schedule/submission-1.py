class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}  # course : list of prerequisites

        for c, pr in prerequisites:
            graph[c].append(pr)
        
        visiting = set()    # check for cycles in the prerequisite list of the current node
        def dfs(node):
            if node in visiting:
                return False
            if node == []:
                return True

            visiting.add(node)

            for pr in graph[node]:
                if not dfs(pr):
                    return False

            visiting.remove(node)
            graph[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

            
            