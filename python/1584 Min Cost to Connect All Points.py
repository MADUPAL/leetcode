class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for src in range(len(points)):
            x1, y1 = points[src]
            for dst in range(src+1, len(points)):
                x2, y2 = points[dst]
                if src != dst:
                    w = abs(x1-x2)+abs(y1-y2)
                    adjList[src].append((dst, w))
                    adjList[dst].append((src, w))
        
        minHeap = [(0, 0)]
        visited = set()
        ans = 0

        while len(visited) != len(points):
            w, src = heapq.heappop(minHeap)

            if src in visited:
                continue
            visited.add(src)
            ans += w

            for dst, nw in adjList[src]:
                if dst not in visited:
                    heapq.heappush(minHeap, (nw, dst))
        
        return ans