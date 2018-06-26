class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = {}
        summe = 0
        
        for i in nums:
            if(i in numbers):
                summe -= i
            else:
                numbers[i] = i
                summe += i
        
        return summe