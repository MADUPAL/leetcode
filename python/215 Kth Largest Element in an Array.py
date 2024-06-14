##### time limit: quick select
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k = len(nums) - k
        # def quickSearch(arr, s, e):
        #     pivot = arr[e]
        #     p = s
            
        #     for i in range(s, e):
        #         if arr[i] <= pivot:
        #             arr[i], arr[p] = arr[p], arr[i]
        #             p += 1
            
        #     arr[e], arr[p] = arr[p], arr[e]

        #     if k < p:
        #         return quickSearch(arr, s, p-1)
        #     elif k > p:
        #         return quickSearch(arr, p+1, e)
        #     else:
        #         return arr[p]
            
        # return quickSearch(nums, 0, len(nums) - 1)
        
        ##### maxHeap
        nums = [-num for num in nums]
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
        
        return -nums[0]