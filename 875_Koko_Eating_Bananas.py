from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # piles: [5, 6, 7]
        # hours: smaller than h
        # return speed: nums / hr
        # Use binary search to find speed
        if not piles:
            return -1
        
        start, end = 1, max(piles)
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if self.countHours(piles, mid) <= h:
                end = mid
            
            else:
                start = mid
        
        # Since start is smaller than end, check the start first
        if self.countHours(piles, start) <= h:
            return start
        
        if self.countHours(piles, end) <= h:
            return end

        return -1
                
                
    def countHours(self, piles, speed) -> int:
        hours = 0
        
        for pile in piles:
            hours += ceil(pile / speed)
        
        return hours
            
        

if __name__ == '__main__':
    sol = Solution()
    result = sol.minEatingSpeed([3,6,7,11], 8)
    print(result)   # 4
    result = sol.minEatingSpeed([30,11,23,4,20], 5)
    print(result)   # 30
    result = sol.minEatingSpeed([30,11,23,4,20], 6)
    print(result)   # 23
    result = sol.minEatingSpeed([312884470], 968709470)
    print(result)   # 1
    