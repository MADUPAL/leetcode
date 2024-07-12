class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s, ans = 0, 0
        L = 0

        for R in range(len(arr)):
            s += arr[R]
            if R-L+1 > k:
                s -= arr[L]
                L += 1
            if R-L+1 == k and s//k >= threshold:
                ans += 1
        
        return ans