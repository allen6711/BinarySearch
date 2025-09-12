class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            # Peak is on the right
            if nums[mid] < nums[mid + 1]:
                start = mid
            
            # Peak is on the left
            elif nums[mid] < nums[mid - 1]:
                end = mid
            
            # nums[mid] >= nums[mid + 1] and nums[mid] >= nums[mid - 1] -> Peak
            else:
                return mid
        
        # start peak(end)
        # peak(start) end
        if nums[start] > nums[end]:
            return start

        else:
            return end
        
if __name__ == '__main__':
    sol = Solution()
    result = sol.findPeakElement([1,2,3,1])
    print(result)
    result = sol.findPeakElement([1,2,1,3,5,6,4])
    print(result)
    result = sol.findPeakElement([1, 2])
    print(result)
    result = sol.findPeakElement([1])
    print(result)
    result = sol.findPeakElement([])
    print(result)