class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        
        while start <= end:
            middle = start + (end - start) // 2
            l, r = 0, len(matrix[middle]) - 1
            while l <= r:
                m = l + (r - l) // 2
                if matrix[middle][m] < target:
                    l = m + 1
                elif matrix[middle][m] > target:
                    r = m - 1
                else:
                    return True
            if r < 0:
                end = middle - 1
            elif l >= len(matrix[middle]):
                start = middle + 1
            else:
                break
        return False