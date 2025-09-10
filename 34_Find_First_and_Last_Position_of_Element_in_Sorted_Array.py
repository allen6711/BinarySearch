class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        
        first_position, last_position = -1, -1
        
        # first position
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < target:
                start = mid
            
            elif nums[mid] > target:
                end = mid
            
            else:
                end = mid
        
        if nums[start] == target:
            first_position = start
        
        elif nums[end] == target:
            first_position = end
        
        # end position
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < target:
                start = mid
            
            elif nums[mid] > target:
                end = mid
            
            else:
                start = mid
        
        if nums[end] == target:
            last_position = end

        elif nums[start] == target:
            last_position = start
        
        return [first_position, last_position]
    
if __name__ == '__main__':
    sol = Solution()
    result = sol.searchRange([5,7,7,8,8,10], 8)
    print(result)
    result = sol.searchRange([5,7,7,8,8,10], 6)
    print(result)
    result = sol.searchRange([5,6, 7,7,8,8,10], 6)
    print(result)
    result = sol.searchRange([2, 2], 2)
    print(result)
    result = sol.searchRange([], 2)
    print(result)
