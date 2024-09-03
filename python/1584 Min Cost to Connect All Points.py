class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        ans = 0
        for src in range(len(points)):
            x1, y1 = points[src]
            for dst in range(src, len(points)):
                x2, y2 = points[dst]
                w = abs(x1-x2)+abs(y1-y2)
                heapq.heappush(minHeap, (w, src, dst))
        
        cnt = 0
        uf = UnionFind(len(points))

        while cnt < len(points)-1:
            w, n1, n2 = heapq.heappop(minHeap)
            if not uf.union(n1, n2):
                continue
            ans += w
            cnt += 1
        
        return ans

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