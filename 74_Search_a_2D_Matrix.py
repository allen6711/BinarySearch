class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        length = m * n
        start, end = 0, length - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if matrix[mid // n][mid % n] <= target:
                start = mid
            
            else:
                end = mid
        
        if matrix[start // n][start % n] == target:
            return True

        if matrix[end // n][end % n] == target:
            return True
        
        return False

if __name__ == '__main__':
    sol = Solution()
    result = sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    print(result)
    result = sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
    print(result)
    result = sol.searchMatrix([[1,3]], 3)
    print(result)
    result = sol.searchMatrix([[]], 3)
    print(result)