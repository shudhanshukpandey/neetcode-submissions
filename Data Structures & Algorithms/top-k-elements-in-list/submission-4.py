class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1st heap

        heap = []

        # heapq.heapify(heap)

        feq_counter = {}

        for i in nums:
            feq_counter[i] = feq_counter.get(i,0)+1
        
        for i in feq_counter:
            heapq.heappush(heap,(-feq_counter[i],i))

        # print(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]
        