class Solution:
    def maxLength(self, ribbons: list[int], k: int) -> int:
        if not ribbons:
            return 0
        
        start, end = 1, max(ribbons)
        #        start, ....   end
        #length: 1, 2, 3,....,max(ribbons)
        #k: sum(ribbons), ......, 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if self.get_pieces(ribbons, mid) >= k:
                start = mid
            
            else:
                end = mid
        
        # If end never moves until the while loop finished
        if self.get_pieces(ribbons, end) >= k:
            return end

        if self.get_pieces(ribbons, start) >= k:
            return start
        
        return 0
        
    
    def get_pieces(self, ribbons, length) -> int:
        pieces = 0
        
        for ribbon in ribbons:
            pieces += ribbon // length
        
        return pieces
    

if __name__ == '__main__':
    sol = Solution()
    result = sol.maxLength([9,7,5], 3)
    print(result)
    result = sol.maxLength([], 3)
    print(result)
    result = sol.maxLength([7,5,9], 4)
    print(result)
    result = sol.maxLength([5,7,9], 22)
    print(result)
    result = sol.maxLength([1, 1, 1, 2], 2)
    print(result)
    ribbons = [100000,100000,100000,100000,
               100000,100000,100000,100000,
               100000,100000,100000,100000,
               100000,100000,100000,100000,
               100000,100000,100000,100000,1,
               100000,100000,100000,100000,
               100000,100000,100000,100000,
               100000,100000,100000,100000,
               100000,100000,100000,100000,
               100000,100000,100000,100000,
               100000,100000,100000,100000,
               100000,100000,100000,100000,100000]
    result = sol.maxLength(ribbons, 49)
    print(result)    #100000