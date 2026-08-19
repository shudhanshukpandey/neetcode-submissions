class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap_list = [-i for i in stones]
        heapq.heapify(heap_list)

        while len(heap_list)>1:
        
            item_a = heapq.heappop(heap_list)
            item_b = heapq.heappop(heap_list)
            
            if item_a!=item_b:
                item_c = abs(item_a-item_b)
                
                heapq.heappush(heap_list, -item_c)
        
        return -heap_list[0] if heap_list else 0
        