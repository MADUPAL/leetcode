class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minPrice = 10001

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                ans = max(ans, price-minPrice)
        
        return ans