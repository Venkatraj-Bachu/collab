# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0

        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1
        getnum = reader
        while left <= right:
            mid = (left+right)//2
            num = getnum.get(mid)
            if num == target:
                return mid
            if num == 2**31 - 1:
                right = mid
            if num < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1