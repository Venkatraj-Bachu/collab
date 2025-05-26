class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(nums) - k

        while left < right:
            mid = (left + right) // 2
            if x - nums[mid] > nums[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return nums[left:left+k]