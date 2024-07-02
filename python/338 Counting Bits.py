class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = []

        # for x in range(n+1):
        #     i = x
        #     cnt = 0
        #     while i > 0:
        #         cnt += i & 1
        #         i >>= 1
        #     ans.append(cnt)
        
        # return ans

        dp = [0] * (n+1)
        p = 1
        for i in range(1, n+1):
            if i == 2*p:
                p *= 2
            dp[i] = dp[i-p] + 1
        
        return dp