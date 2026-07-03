class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        feq = defaultdict(int)

        for i in nums:
            feq[i] = feq.get(i,0)+1

        result = dict(sorted(feq.items(), key=lambda x: (-x[1], x[0])))
        # print(result)
        return list(result.keys())[:k]
        