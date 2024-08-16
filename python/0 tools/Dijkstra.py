class Solution:
    def Djikstra(self, edges: List[List[int]], n: int, start: int) -> int:
        adjList = defaultdict(list)
        for src, dst, w in edges:
            adjList[src].append((dst, w))
        
        minHeap = [(0, start)]
        shortest = {}

        while minHeap:
            w, v = heapq.heappop(minHeap)
            if v in shortest:
                continue
            shortest[v] = w

            for nv, nw in adjList[v]:
                if nv not in shortest:
                    heapq.heappush(minHeap, (w+nw, nv))
        
        return shortest