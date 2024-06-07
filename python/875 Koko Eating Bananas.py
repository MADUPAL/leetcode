class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # def isCorrect(m):
        #     t = 0
        #     for i in piles:
        #         Q, R = divmod(i, m)
        #         Q = Q + 1 if R != 0 else Q
        #         t += Q
            
        #     if t <= h:
        #         return -1
        #     elif t > h:
        #         return 1

        # def binarySearch(l, r):

        #     rslt = max(piles)
        #     while l <= r:
        #         k = (l+r)//2
        #         res = isCorrect(k)
        #         if res > 0:
        #             l = k + 1
        #         else:
        #             r = k - 1
        #             rslt = min(rslt, k)
        #     return rslt
        
        # return binarySearch(1, max(piles))

        l, r = 1, max(piles)

        ans = 0
        while l <= r:
            k = (l+r)//2

            t = 0
            for pile in piles:
                t += math.ceil(pile/k)
                # t += pile//k
                # t += 0 if pile%k == 0 else 1
                        
            if t > h:
                l = k+1
            elif t <= h:
                r = k-1
                ans = k
        
        return ans

        l, r = 1, max(piles)
        rslt = r

        while l <= r:
            k = (l+r)//2
            t = 0
            for i in piles:
                t += math.ceil(i/k)
            
            if t > h:
                l = k + 1
            else:
                r = k - 1
                rslt = min(rslt, k)
        
        return rslt