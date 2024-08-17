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
    
        # visited = set()
        # path = set()

        # def dfs(src):
        #     if src in path:
        #         return False
        #     if src in visited:
        #         return True
        #     visited.add(src)
        #     path.add(src)
        #     for nei in adjList[src]:
        #         if not dfs(nei):
        #             return False

        #     path.remove(src)
        #     return True
        
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        
        # return True