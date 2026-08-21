class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)

        while k:
            return_data = heapq.heappop(heap)
            k-=1
        return -return_data

        