class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i =0
        len_arr = len(arr)

        while i<len_arr-1:
            arr[i] = max(arr[i+1:])
            i+=1
        arr[-1]=-1
        # print(arr)
        return arr