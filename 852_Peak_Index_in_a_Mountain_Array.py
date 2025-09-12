class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        if not arr:
            return -1

        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            # Move right bound to mid. Since arr[mid] > arr[mid+1], mid is at/after the peak,
            # so peak <= mid and end never crosses to the index before the peak.
            if arr[mid] > arr[mid + 1]:
                end = mid
            
            else:
                start = mid
        
        return end

if __name__ == '__main__':
    sol = Solution()
    result = sol.peakIndexInMountainArray([0,1,0])
    print(result)
    result = sol.peakIndexInMountainArray([0,2,1,0])
    print(result)
    result = sol.peakIndexInMountainArray([0,10,5,2])
    print(result)