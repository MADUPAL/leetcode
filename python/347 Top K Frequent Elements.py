class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hm = {}
        # for n in nums:
        #     if n not in hm:
        #         hm[n] = 0
        #     hm[n] += 1
        
        # sortedHm = sorted(hm.items(), key=lambda x:-x[1])

        # ans = []
        # for key, v in sortedHm:
        #     ans.append(key)
        #     k -= 1
        #     if k <= 0:
        #         break
        # return ans

        # counts = [[] for _ in range(len(nums)+1)]
        # hm = {}

        # for n in nums:
        #     if n not in hm:
        #         hm[n] = 0
        #     hm[n] += 1
        
        # for key, val in hm.items():
        #     counts[val].append(key)

        # ans = []
        # for i in range(len(counts)-1, -1, -1):
        #     for n in counts[i]:
        #         ans.append(n)
        #         if len(ans) == k:
        #             return ans

        hm = {}
        for n in nums:
            if n not in hm:
                hm[n] = 0
            hm[n] += 1
        
        maxheap = []
        for key, val in hm.items():
            heapq.heappush(maxheap, [-val, key])

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(maxheap)[1])
        
        return ans