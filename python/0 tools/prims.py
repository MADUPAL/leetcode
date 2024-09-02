class Solution:
	def Prims(self, points: List[List[int]], start: int) -> int:
		n = len(points)

		adjList = defaultdict(list)

		for i in range(n):
			for j in range(i+1, n):
				dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
				adjList[i].append((j, dist))
				adjList[j].append((i, dist))

		minHeap = []
		for nv, nw in adjList[start]:
			heapq.heappush(minHeap, (w, start, nv))

		visited = set()
		visited.add(start)

		mst = []
		# while len(visited) != n:
		while minHeap:
			w, src, dst  = heapq.heappop(minHeap)
			if dst in visited:
				continue
			
			visited.add(dst)
			mst.append([src, dst])

			for nv, nw in adjList[dst]:
				if nv not in visited:
					heapq.heappush(minHeap, (nw, dst, nv))

		return mst