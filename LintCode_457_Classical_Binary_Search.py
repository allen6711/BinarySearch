"""
Find any position of a target number in a sorted array. Return -1 if target does not exist.
Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 1 or 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1
Challenge
O(logn) time


"""
class Solution:
    def findPosition(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            # keep start at the last position of target values (only if nums[end] == target)
            if nums[mid] <= target:
                start = mid
            
            else:
                end = mid
        
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end

        return -1
        
if __name__ == '__main__':
    sol = Solution()
    result = sol.findPosition([1,2,2,4,5,5], 2)
    print(result)
    result = sol.findPosition([1,2,2,4,5,5], 6)
    print(result)
    result = sol.findPosition([], 2)
    print(result)