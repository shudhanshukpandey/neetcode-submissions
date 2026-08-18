import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Store all elements as negative numbers to simulate a max-heap
        self._heap = [-x for x in nums]
        self._k = k
        heapq.heapify(self._heap)

    def add(self, val: int) -> int:
        # Push the negative value without popping anything
        heapq.heappush(self._heap, -val)
        
        # Find the k-th smallest element from our inverted heap
        # and flip its sign back to positive
        kth_neg_val = heapq.nsmallest(self._k, self._heap)[-1]
        return -kth_neg_val
