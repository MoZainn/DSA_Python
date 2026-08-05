class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        max_rob = [0] * n
        max_rob[0] = nums[0]
        max_rob[1] = max(nums[0], nums[1])

        for i in range(2, n):
            max_rob[i] = max(max_rob[i-1], max_rob[i-2] + nums[i])
        
        return max_rob[-1]
