class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ans, L = 0, 0
        # cnt = {}

        # for R in range(len(s)):
        #     if s[R] not in cnt:
        #         cnt[s[R]] = 0
        #     cnt[s[R]] += 1

        #     maxF = max(cnt, key = cnt.get)
        #     if R-L+1 - cnt[maxF] <= k:
        #         ans = max(ans, R-L+1)
        #     else:
        #         cnt[s[L]] -= 1
        #         L += 1
        
        # return ans

        ans, l = 0, 0
        cnt = {}

        for r in range(len(s)):
            if s[r] not in cnt:
                cnt[s[r]] = 0
            cnt[s[r]] += 1

            if r-l+1 - max(cnt.values()) <= k:
                ans = max(ans, r-l+1)
            else:
                cnt[s[l]] -= 1
                l += 1
        
        return ans