class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def solve(idx):
            if idx == n:
                return [[]]
            perms = solve(idx+1)
            newPerms = []

            for p in perms:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i, nums[idx])
                    newPerms.append(pCopy)
            
            return newPerms
        
        return solve(0)
    
        # n = len(nums)
        # ans = []
        # visited = [0] * n

        # def solve(idx, p):
        #     if len(p) == n:
        #         ans.append(p.copy())
        #         return
            
        #     for i in range(n):
        #         if visited[i] == 0:
        #             p.append(nums[i])
        #             visited[i] = 1
        #             solve(idx+1, p)
        #             visited[i] = 0
        #             p.pop()
        # solve(0, [])

        # return ans