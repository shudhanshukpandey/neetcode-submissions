class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row_data in matrix:
            if target in row_data:
                return True
        return False
        