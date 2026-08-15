class Solution:
    def countBits(self, n: int) -> List[int]:

        response_data = []

        for i in range(n+1):

            counter = 0

            while i:
                counter+=1 if i&1 else 0
                i>>=1
            response_data.append(counter)
        return response_data

        