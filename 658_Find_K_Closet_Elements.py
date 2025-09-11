class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # find the first position of greater than target
        right = self.find_upper_closest(arr, x)
        left = right - 1
        
        for _ in range(k):
            if self.is_left_closer(arr, x, left, right):
                left -= 1
            
            else:
                right += 1
        
        return arr[left + 1: right]
        
    
    def find_upper_closest(self, arr, x):
        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if arr[mid] >= x:
                end = mid
            
            else:
                start = mid
        
        # If all num in arr are greater than x, then this condiiton
        # [2, 3, 4], x = 1
        if arr[start] >= x:
            return start
        
        # Generally is this
        if arr[end] >= x:
            return end

        # All elements are < x, so the insertion index is len(arr)
        return len(arr)

    def is_left_closer(self, arr, x, left, right):
        if left < 0:
            return False
        
        if right >= len(arr):
            return True

        return x - arr[left] <= arr[right] - x


if __name__ == '__main__':
    sol = Solution()
    result = sol.findClosestElements([1,2,3,4,5], 4, 3)
    print(result)
    result = sol.findClosestElements([1,1,2,3,4,5], k = 4, x = -1)
    print(result)
    result = sol.findClosestElements([2, 3, 4], k = 2, x = 1)
    print(result)
    result = sol.findClosestElements([2], k = 1, x = 1)
    print(result)