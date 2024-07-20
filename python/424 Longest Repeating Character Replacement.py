class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, L = 0, 0
        cnt = {}

        for R in range(len(s)):
            if s[R] not in cnt:
                cnt[s[R]] = 0
            cnt[s[R]] += 1

            maxF = max(cnt, key = cnt.get)
            if R-L+1 - cnt[maxF] <= k:
                ans = max(ans, R-L+1)
            else:
                cnt[s[L]] -= 1
                L += 1
        
        return ans