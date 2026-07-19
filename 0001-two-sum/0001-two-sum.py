class Solution(object):
    def twoSum(self, nums, target):
        Hash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in Hash:
                return [Hash[complement], i]
            Hash[num] = i

        return []
        