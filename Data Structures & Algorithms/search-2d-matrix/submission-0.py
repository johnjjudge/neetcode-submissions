class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix)
        width = len(matrix[0])
        
        solution_row = []
        for row in matrix:
            if target == row[0] or target == row[-1]:
                return True
            elif target > row[0] and target < row[-1]:
                solution_row = row
                break
        
        if solution_row == []:
            return False
        
        low = 0
        high = len(solution_row) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if solution_row[mid] < target:
                low = mid + 1
            elif solution_row[mid] > target:
                high = mid - 1
            else:
                return True
        
        return False