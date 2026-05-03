class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left = 0
        right = (rows-1)*cols + (cols - 1)

        while left <= right:
            med = (left + right) // 2
            j = med % cols
            i = (med - j) // cols
            if target == matrix[i][j]:
                return True
            if target > matrix[i][j]:
                left = med  + 1
            else:
                right = med - 1
        return False