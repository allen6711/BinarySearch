class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums)
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < target:
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
    result = sol.search([-1,0,3,5,9,12], 9)
    print(result)
    result = sol.search([-1,0,3,5,9,12], 2)
    print(result)
    result = sol.search([], 1)
    print(result)
    result = sol.search([1, 2], 2)
    print(result)
    result = sol.search([1], 1)
    print(result)