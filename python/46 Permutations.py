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