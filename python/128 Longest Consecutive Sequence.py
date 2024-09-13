class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ### not O(n)
        # hm = defaultdict(list)
        # visited = set()

        # for n in nums:
        #     hm[n].append(n-1)
        #     hm[n].append(n+1)
        
        # def dfs(key):
        #     if key not in hm or key in visited:
        #         return 0
            
        #     visited.add(key)
        #     return 1+dfs(hm[key][0])+dfs(hm[key][1])
        
        # ans = 0
        # for n in nums:
        #     ans = max(ans, dfs(n))
        
        # return ans

        numSet = set(nums)

        ans = 0
        for n in numSet:
            if n-1 in numSet:
                continue
            length = 0
            while n+length in numSet:
                length += 1
            ans = max(ans, length)
        
        return ans
    
        # nums = set(nums)
        # ans = 0

        # for n in nums:
        #     print(n)
        #     if n-1 not in nums:
        #         l = 0
        #         while n in nums:
        #             l += 1
        #             n += 1
        #         ans = max(l, ans)
        #     if n+1 not in nums:
        #         l = 0
        #         while n in nums:
        #             l += 1
        #             n -= 1
        #         ans = max(l, ans)
        
        # return ans

        # nums = set(nums)
        # ans = 0

        # for n in nums:
        #     if n-1 in nums:
        #         continue
        #     l = 0
        #     while n in nums:
        #         l += 1
        #         n += 1
        #     ans = max(l, ans)
        
        # return ans