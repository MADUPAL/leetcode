class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(curMax, 0)
            curMin = min(curMin, 0)
            curMax += n
            curMin += n
            total += n
            maxSum = max(curMax, maxSum)
            minSum = min(curMin, minSum)
        
        return maxSum if maxSum < 0 else max(total-minSum, maxSum)
    
        # maxSum, minSum = nums[0], nums[0]
        # curMax, curMin = 0, 0
        # total = 0

        # for n in nums:
        #     curMax = max(curMax+n, n)
        #     curMin = min(curMin+n, n)
        #     maxSum = max(maxSum, curMax)
        #     minSum = min(minSum, curMin)
        #     total += n
        
        # return maxSum if maxSum < 0 else max(total-minSum, maxSum)