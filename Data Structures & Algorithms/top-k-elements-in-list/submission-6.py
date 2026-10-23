class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1st heap

        # heap = []

        # #heapq.heapify(heap) only when list is already there, no need in thi  case

        # feq_counter = {}

        # for i in nums:
        #     feq_counter[i] = feq_counter.get(i,0)+1
        
        # for i in feq_counter:
        #     heapq.heappush(heap,(-feq_counter[i],i))


        # return [heapq.heappop(heap)[1] for i in range(k)]

        # 2nd bucket
        output = []
        bucket = [[] for _ in range(len(nums))]

        feq = {}
        
        for i in nums:
            feq[i] = feq.get(i, 0) +1

        for i in feq:
            bucket[feq[i]-1].append(i)
        # print(feq)
        # print(bucket, bucket[::-1])
        for i in bucket[::-1]:

            if i and len(output)!=k:
                # print(k, i)
                output += i
                
        
        return output
        


        
            