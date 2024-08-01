class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []

        def solve(opened, closed):
            if opened == closed == n:
                ans.append(''.join(stack))
                return
            
            if opened < n:
                stack.append("(")
                solve(opened+1, closed)
                stack.pop()
            if opened > closed:
                stack.append(")")
                solve(opened, closed+1)
                stack.pop()

        solve(0, 0)
        return ans