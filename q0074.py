class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col, row = len(matrix[0]), len(matrix)
        start = 0
        end = col * row -1
        while start <= end:
            if end <= start + 1:
                return target == matrix[start/col][start%col] or target == matrix[end/col][end%col]
            if target == matrix[start/col][start%col]: return True
            if target == matrix[end/col][end%col]: return True
            mid = (start + end) //2
            if target == matrix[mid/col][mid%col]: return True
            if target > matrix[mid/col][mid%col]:
                start = mid + 1
            else:
                end = mid -1
        return False