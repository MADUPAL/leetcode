class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)
        for i, [src, dst] in enumerate(edges):
            adjList[src].append([dst, succProb[i]])
            adjList[dst].append([src, succProb[i]])
        
        maxHeap = [(-1, start_node)]
        visited = set()

        while maxHeap:
            w, v = heapq.heappop(maxHeap)
            if v in visited:
                continue
            visited.add(v)
            if v == end_node:
                return -1 * w
            for nv, nw in adjList[v]:
                if nv not in visited:
                    heapq.heappush(maxHeap, (w*nw, nv))
        
        return 0