class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2

            # we need two conditions to seperate the nums
            # [4, 5, 6, 7] and [0, 1, 2]
            # to control mid correctly
            if target <= nums[-1]:
                #[xxxxx012345]
                # 2 situations: nums[mid] in the first part or the second part
                # second part
                if target <= nums[mid] <= nums[-1]:
                    end = mid
                
                # nums[mid] < target or
                # nums[-1] < nums[mid]
                # both should move start to mid
                else:
                    start = mid
            
            # target > nums[-1]
            else:
                if nums[-1] < nums[mid] <= target:
                    start = mid
                
                # target < nums[mid] or
                # nums[mid] <= nums[-1]
                else:
                    end = mid
        
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end
        
        return -1
    
if __name__ == '__main__':
    sol = Solution()
    result = sol.search([4,5,6,7,0,1,2], 0)
    print(result)
    result = sol.search([4,5,6,7,0,1,2], 3)
    print(result)
    result = sol.search([7,0,1,2], 0)
    print(result)
    result = sol.search([0,1,2], 0)
    print(result)
    result = sol.search([1], 0)
    print(result)
    result = sol.search([], 1)
    print(result)