class Solution:
    def checkIfPrerequisite(self, numCourses: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        for src, dst in pre:
            adjList[src].append(dst)

        visited = set()
        path = {}

        def dfs(src):
            if src in visited:
                return
            
            visited.add(src)
            path[src] = set()

            for dst in adjList[src]:
                path[src].add(dst)
                dfs(dst)
                for n in path[dst]:
                    path[src].add(n)
        
        for i in range(numCourses):
            dfs(i)
        
        ans = []
        for src, dst in queries:
            ans.append(dst in path[src])
        
        return ans