class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntS, cntT = {}, {}
        for c in t:
            cntT[c] = 1 + cntT.get(c, 0)
        
        l = 0
        check = 0
        need = len(cntT)
        maxLen = 100001
        ans = [-1, -1]

        for r in range(len(s)):
            c = s[r]
            cntS[c] = 1 + cntS.get(c, 0)

            if c in cntT and cntS[c] == cntT[c]:
                check += 1
                
            while check == need:
                if maxLen > r-l+1:
                    maxLen = r-l+1
                    ans = [l, r]
                cntS[s[l]] -= 1
                if s[l] in cntT and cntS[s[l]] < cntT[s[l]]:
                    check -= 1
                l += 1
        l, r = ans
        return "" if maxLen == 100001 else s[l:r+1]