class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1
        target_row = 0

        while row_l <= row_r:
            mid_row = (row_l + row_r) // 2
            if target < matrix[mid_row][0]:
                row_r = mid_row - 1
            elif target > matrix[mid_row][-1]:
                row_l = mid_row + 1
            else:
                target_row = mid_row
                break
        
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[target_row][mid]:
                right = mid - 1
            elif target > matrix[target_row][mid]:
                left = mid + 1
            else:
                return True
            
        return False