class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        count = Counter(nums)
        nums = sorted(list(set(nums)))

        prev_max1 = 0
        prev_max2 = 0

        for i in range(len(nums)):
            cur_sum = nums[i] * count[nums[i]]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = prev_max2
                prev_max2 = max(cur_sum + prev_max1, prev_max2)
                prev_max1 = temp
            else:
                temp = prev_max2
                prev_max2 = cur_sum + prev_max2
                prev_max1 = temp

        return prev_max2