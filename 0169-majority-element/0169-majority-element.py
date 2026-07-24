class Solution(object):
    def majorityElement(self, nums):
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
            
        for i in hash:
            if hash[i] > len(nums) // 2:
                return i
