class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum
    
        # maxSum, curSum = -10001, 0

        # for n in nums:
        #     curSum = max(n, curSum+n)
        #     maxSum = max(maxSum, curSum)
        
        # return maxSum