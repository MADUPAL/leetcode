### without cycle
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for x, y in edges:
            adjList[x].append((y))
        
        visited = set()
        topSort = []

        def dfs(src):
            if src in visited:
                return
            visited.add(src)
            for nei in adjList[src]:
                dfs(nei)
            topSort.append(src)
            return True
        
        for i in range(n):
          dfs(i)
        topSort.reverse()
        return topSort

### with cycle
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for x, y in edges:
            adjList[x].append((y))
        
        visited = set()
        topSort = []
        path = set()

        def dfs(src):
            if src in path:
                return False
            if src in visited:
                return True
            visited.add(src)
            path.add(src)
            for nei in adjList[src]:
                if not dfs(nei):
                    return False
            topSort.append(src)
            path.remove(src)
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        # topSort.reverse()
        return topSort