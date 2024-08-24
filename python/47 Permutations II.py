class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        permu = []

        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] = 0
            cnt[num] += 1

        def permutes():
            if len(permu) == len(nums):
                ans.append(permu.copy())
                return
            
            for num in cnt.keys():
                if cnt[num]:
                    permu.append(num)
                    cnt[num] -= 1
                    permutes()

                    permu.pop()
                    cnt[num] += 1
        permutes()
        return ans
    
        # cnt = {}
        # for n in nums:
        #     if n not in cnt:
        #         cnt[n] = 0
        #     cnt[n] += 1
        
        # ans = []
        # def solve(p):
        #     if len(p) >= len(nums):
        #         ans.append(p.copy())
        #         return

        #     for n in cnt.keys():
        #         if cnt[n]:
        #             cnt[n] -= 1
        #             p.append(n)
        #             solve(p)
        #             cnt[n] += 1
        #             p.pop()

        # solve([])
        # return ans