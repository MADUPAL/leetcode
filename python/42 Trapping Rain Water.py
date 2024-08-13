class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height)-1

        ans = 0
        maxL = height[0]
        maxR = height[-1]
        while L < R:
            if maxL <= maxR:
                L += 1
                maxL = max(maxL, height[L])
                ans += max(0, maxL - height[L])
            else:
                R -= 1
                maxR = max(maxR, height[R])
                ans += max(0, maxR - height[R])
        
        return ans

        # L, R = 0, len(height)-1
        # maxL, maxR = height[0], height[-1]

        # water = 0
        # while L < R:
        #     if maxL <= maxR:
        #         L += 1
        #         maxL = max(maxL, height[L])
        #         water += maxL-height[L]
        #     else:
        #         R -= 1
        #         maxR = max(maxR, height[R])
        #         water += maxR-height[R]
        
        # return water