class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        alreadySeen = {}
        
        for i in range(0, len(nums)):
            need = target - nums[i]
            if(need in alreadySeen):
                return [alreadySeen[need], i]
            else:
                alreadySeen[nums[i]] = i