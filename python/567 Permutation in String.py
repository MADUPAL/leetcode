class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = {}
        cnt2 = {}

        keys = [chr(c+ord('a')) for c in range(26)]

        for key in keys:
            cnt1[key] = 0
            cnt2[key] = 0

        for c in s1:
            cnt1[c] += 1
        
        l = 0
        for c in s2[0:len(s1)]:
            cnt2[c] += 1

        for r in range(len(s1), len(s2)):
            if cnt1 == cnt2:
                return True
            cnt2[s2[l]] -= 1
            cnt2[s2[r]] += 1
            # print(cnt1, cnt2)
            l += 1
            
        return cnt1 == cnt2