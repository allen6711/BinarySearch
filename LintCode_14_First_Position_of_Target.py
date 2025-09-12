"""
Description
Given a sorted array (ascending order) and a target number, find the first index of this number in O(logn) time complexity.
If the target number does not exist in the array, return -1.

Example
Example 1:
Input:
tuple = [1,4,4,5,7,7,8,9,9,10]
target = 1
Output: 0
Explanation: The first index of 1 is 0.

Example 2:
Input: tuple = [1, 2, 3, 3, 4, 5, 10]
target = 3
Output: 2
Explanation: The first index of 3 is 2.

Example 3:
Input: tuple = [1, 2, 3, 3, 4, 5, 10]
target = 6
Output: -1
Explanation: here is no 6 in the array, return -1.

"""
class Solution:
    def bs_first(self, nums: list[int], target) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] >= target:
                end = mid
            
            else:
                start = mid
        
        if nums[start] == target:
            return start

        if nums[end] == target:
            return end
        
        return -1
    
if __name__ == '__main__':
    sol = Solution()
    result = sol.bs_first([1,4,4,5,7,7,8,9,9,10], 1)
    print(result)
    result = sol.bs_first([1, 2, 3, 3, 4, 5, 10], 3)
    print(result)
    result = sol.bs_first([3, 3, 3, 3, 3], 3)
    print(result)
    result = sol.bs_first([1, 2, 3, 3, 4, 5, 10], 6)
    print(result)
    result = sol.bs_first([], 6)
    print(result)