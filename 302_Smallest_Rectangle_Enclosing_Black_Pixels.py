class Solution:
    def minArea(self, image: list[list[int]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        if m == 0 or n == 0:
            return 0
        
        # Right column (we need to consider y to avoid it is the only one)
        start, end = y, n - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if self.checkColumn(image, mid):
                # last position of elements fitting condition
                start = mid
            
            else:
                end = mid
        
        
        # print(start, end)
        # Check the bounder and return the right
        right = end if self.checkColumn(image, end) else start
        
        # Left Column (we need to consider y to avoid it is the only one)
        start, end = 0, y
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if self.checkColumn(image, mid):
                # first position of elements fitting condition
                end = mid
            
            else:
                start = mid
        
        # print(start, end)
        # Check the bounder and return the left
        left = start if self.checkColumn(image, start) else end
        
        # Up Row (we need to consider x to avoid it is the only one)
        start, end = 0, x
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if self.checkRow(image, mid):
                # first position of elements fitting condition
                end = mid
            
            else:
                start = mid
        
        # print(start, end)
        # Check the bounder and return the up
        up = start if self.checkRow(image, start) else end
        
        # Down Row (we need to consider x to avoid it it the only one)
        start, end = x, m - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if self.checkRow(image, mid):
                # last position of elements fitting condition
                start = mid
            
            else:
                end = mid
        
        # print(start, end)
        # Check the bounder and return the down
        down = end if self.checkRow(image, end) else start
        
        return (right - left + 1) * (down - up + 1)
    
    def checkColumn(self, image, col) -> bool:
        for i in range(len(image)):
            if image[i][col] == "1":
                return True
        
        return False
    
    def checkRow(self, image, row) -> bool:
        for j in range(len(image[0])):
            if image[row][j] == "1":
                return True
        
        return False

if __name__ == '__main__':
    sol = Solution()
    image = [["0", "0", "1", "0"],
             ["0", "1", "1", "0"],
             ["0", "1", "0", "0"]]
    result = sol.minArea(image, 0, 2)
    print(result)
    image = [["1", "1", "1", "0"],
             ["1", "1", "0", "0"],
             ["0", "0", "0", "0"]]
    result = sol.minArea(image, 0, 1)
    print(result)
    image = [["1"]]
    result = sol.minArea(image, 0, 0)
    print(result)