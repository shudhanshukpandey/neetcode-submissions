class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)

        threshold = len_nums//3

        feq = defaultdict(int)
        response_data = set()

        for val in nums:
            feq[val] = feq.get(val,0)+1

            if feq[val]> threshold:
                response_data.add(val)
        return list(response_data)

