class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def bs(lb, rb, first):
            left = lb
            right = rb
            mid = -1
            while left <= right:
                mid = left +(right - left) // 2
                if nums[mid] == target:
                    if first:
                        while mid > left and nums[mid - 1] == target:
                            mid -= 1
                        return mid

                        # if mid == 0 or nums[mid - 1] < target:
                        #     return mid
                        # right = mid - 1

                    else:
                        while mid < right and nums[mid + 1] == target:
                            mid += 1
                        return mid
                        # if mid == right or nums[mid + 1] > target:
                        #     return mid
                        # left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        first = bs(0, len(nums)-1, True)
        res = []
        if first != -1 and nums[first] == target:
            res.append(first)
            res.append(bs(0, len(nums)-1, False))
            return res
        else:
            return [-1,-1]