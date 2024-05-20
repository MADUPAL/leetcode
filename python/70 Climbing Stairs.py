class Solution:
    # s = [0] * 46
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]

        # if n <= 1:
        #     return 1
        
        # s1 = self.s[n-1] if self.s[n-1] else self.climbStairs(n-1)
        # s2 = self.s[n-2] if self.s[n-2] else self.climbStairs(n-2)

        # self.s[n] = s1 + s2
        # return self.s[n]

        one = 1
        two = 1

        for _ in range(n-1):
            one, two = one + two, one
        
        return one