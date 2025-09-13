class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if not nums:
            return False
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            # target is at the second part
            if target < nums[end]:
                if nums[mid] <= target:
                    start = mid
                
                elif target < nums[mid] < nums[end]:
                    end = mid
                
                # nums[mid] == nums[end]
                # target not in nums
                else:
                    end -= 1
            
            elif target > nums[end]:
                if target <= nums[mid]:
                    end = mid
                
                elif nums[end] < nums[mid] < target:
                    start = mid
                
                # nums[mid] == nums[end]
                # nums not in nums
                else:
                    end -= 1
            
            # target == nums[end]
            else:
                return True
        
        if nums[start] == target:
            return True
        
        if nums[end] == target:
            return False
        
        return False

if __name__ == '__main__':
    sol = Solution()
    result = sol.search([2,5,6,0,0,1,2], 0)
    print(result)
    result = sol.search([2,5,6,0,0,1,2], 3)
    print(result)
    result = sol.search([1, 1, 3], 4)
    print(result)
    result = sol.search([1,1,1,1,1,1,1,1,1], 13)
    print(result)
    result = sol.search([3, 1, 1, 1, 1], 3)
    print(result)