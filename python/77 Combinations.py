class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def comb(idx, cur):
            if len(cur) == k:
                ans.append(cur.copy())
                return
            if idx > n:
                return
            
            for i in range(idx, n+1):
                cur.append(i)
                comb(i+1, cur)
                cur.pop()
        
        comb(1, [])

        return ans