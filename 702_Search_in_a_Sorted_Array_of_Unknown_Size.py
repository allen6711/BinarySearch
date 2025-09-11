class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        """
        Returns arr[index] if index is in range.
        Otherwise returns a sentinel (2**31 - 1) to simulate unknown size.
        """
        if 0 <= index < len(self.arr):
            return self.arr[index]
        return (1 << 31) - 1  # 2**31 - 1

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        index = 1
        
        while reader.get(index) < target:
            index = index * 2
        
        start, end = 0, index
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if reader.get(mid) < target:
                start = mid
            
            else:
                end = mid
        
        if reader.get(start) == target:
            return start

        if reader.get(end) == target:
            return end

        return -1

if __name__ == '__main__':
    sol = Solution()
    reader = ArrayReader([-1,0,3,5,9,12])
    result = sol.search(reader, 9)
    print(result)
    reader = ArrayReader([-1,0,3,5,9,12])
    result = sol.search(reader, 2)
    print(result)
                