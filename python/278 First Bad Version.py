# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        # res = r
        res = 1

        while l <= r:
            m = (l+r)//2
            isBad = isBadVersion(m)

            if isBad:
                r = m - 1
                # res = min(res, m)
                res = m
            else:
                l = m + 1
        
        return res