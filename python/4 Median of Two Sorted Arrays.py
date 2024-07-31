class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        total = len(A)+len(B)
        half = total//2

        if len(A) < len(B):
            A, B = B, A
        
        l, r = 0, len(B)-1
        while True:
            i = (l+r)//2
            j = half-i-2

            Bleft = B[i] if i >= 0 else float("-infinity")
            Bright = B[i+1] if i+1 < len(B) else float("infinity")
            Aleft = A[j] if j >= 0 else float("-infinity")
            Aright = A[j+1] if j+1 < len(A) else float("infinity")

            if Aleft > Bright:
                l = i+1
            elif Aright < Bleft:
                r = i-1
            else:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                else:
                    return min(Aright, Bright) / 1.0
