class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] <= nums[-1]:
                end = mid
            
            else:
                start = mid
        
        return min(nums[start], nums[end])
    
if __name__ == '__main__':
    sol = Solution()
    result = sol.findMin([3,4,5,1,2])
    print(result)
    result = sol.findMin([4,5,6,7,0,1,2])
    print(result)
    result = sol.findMin([11,13,15,17])
    print(result)