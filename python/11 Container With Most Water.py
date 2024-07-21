class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        ans = 0

        while L < R:
            ans = max((R-L)*min(height[L], height[R]), ans)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return ans