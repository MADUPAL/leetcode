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