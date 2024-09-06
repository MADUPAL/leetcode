class Solution:
    def findOrder(self, nums: int, pre: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for src, dst in pre:
            adjList[src].append(dst)
        
        visited, path = set(), set()
        topSort = []

        def dfs(start):
            if start in path:
                return False
            if start in visited:
                return True
            
            visited.add(start)
            path.add(start)

            for nxt in adjList[start]:
                if not dfs(nxt):
                    return False

            topSort.append(start)
            path.remove(start)

            return True
        

        for i in range(nums):
            if not dfs(i):
                return []
        
        return topSort