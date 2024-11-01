class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = { '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz" }

        ans = []
        def letters(idx, cur):
            if idx == len(digits):
                ans.append(''.join(cur))
                return
            
            for s in nums[digits[idx]]:
                cur.append(s)
                letters(idx+1, cur)
                cur.pop()
        if digits:
            letters(0, [])
        return ans