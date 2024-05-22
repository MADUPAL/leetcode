class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr, s, e):
            if s == e:
                return arr
            
            m = (s + e) // 2
            mergeSort(arr, s, m)
            mergeSort(arr, m + 1, e)

            merge(arr, s, m, e)

            return arr
        
        def merge(arr, s, m, e):
            left = arr[s:m+1]
            right = arr[m+1:e+1]
            i, l, r = s, 0, 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    arr[i] = left[l]
                    l += 1
                else:
                    arr[i] = right[r]
                    r += 1
                i += 1
            
            while l < len(left):
                arr[i] = left[l]
                i += 1
                l += 1
            
            while r < len(right):
                arr[i] = right[r]
                i += 1
                r += 1

        return mergeSort(nums, 0, len(nums)-1)