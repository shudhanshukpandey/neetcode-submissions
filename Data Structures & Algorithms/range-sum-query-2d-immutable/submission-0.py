class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_data = 0
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                # print(i,j, self._matrix[i][j])
                sum_data+= self._matrix[i][j]
        # print(sum_data)
        # print("############")
        return sum_data
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)