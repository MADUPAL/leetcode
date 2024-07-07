class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 1
        ans = 1
        prev = ""

        while R < len(arr):
            if arr[R-1] > arr[R] and prev != ">":
                ans = max(ans, R-L+1)
                R += 1
                prev = ">"
            elif arr[R-1] < arr[R] and prev != "<":
                ans = max(ans, R-L+1)
                R += 1
                prev = "<"
            else:
                if arr[R-1] == arr[R]:
                    R += 1
                L = R-1
                prev = ""
        
        return ans