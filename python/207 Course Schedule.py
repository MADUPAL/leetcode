class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjList = {}
        # for src, dst in prerequisites:
        #     if src not in adjList:
        #         adjList[src] = []
        #     if dst not in adjList:
        #         adjList[dst] = []
        #     adjList[src].append(dst)
        adjList = {i : [] for i in range(numCourses)}
        for src, dst in prerequisites:
            adjList[src].append(dst)

        visited = set()
        def dfs(node):
            if not adjList[node]:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for n in adjList[node]:
                if not dfs(n):
                    return False
            visited.remove(node)
            adjList[node] = []
            return True
            
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True