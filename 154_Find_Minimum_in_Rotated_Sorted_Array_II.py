class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < nums[end]:
                end = mid
            
            elif nums[mid] > nums[end]:
                start = mid
            
            else:
                end -= 1
        
        return min(nums[start], nums[end])
        
        
if __name__ == '__main__':
    sol = Solution()
    result = sol.findMin([1,3,5])
    print(result)
    result = sol.findMin([])
    print(result)
    result = sol.findMin([2,2,2,0,1])
    print(result)
    result = sol.findMin([2,2,2,0,2])
    print(result)