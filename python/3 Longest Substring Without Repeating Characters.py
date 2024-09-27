class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, ans = 0, 0
        chars = set()

        for R in range(len(s)):
            while s[R] in chars:
                chars.remove(s[L])
                L += 1
            chars.add(s[R])
            ans = max(ans, len(chars))
        
        return ans

        # l, r = 0, 0

        # check = set()
        # ans = 0

        # for r in range(len(s)):
        #     while s[r] in check:
        #         check.remove(s[l])
        #         l += 1
            
        #     if s[r] not in check:
        #         check.add(s[r])
        #         ans = max(ans, r-l+1)
                
        # return ans