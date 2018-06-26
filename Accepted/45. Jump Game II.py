    def jump(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) <= 1):
            return 0
        
        counterToEnd = 1
        
        index = 0
        
        startFrame = 0
        endFrame = nums[startFrame]
        maximalFromFrame = endFrame
        
        
        while endFrame < len(nums)-1:
            if(index < endFrame):
                testMax = index + nums[index]
                if(testMax > maximalFromFrame):
                    maximalFromFrame = testMax
            else:
                startFrame = endFrame
                endFrame = max(maximalFromFrame, endFrame + nums[endFrame])
                counterToEnd += 1
            index += 1
            
        return counterToEnd


print jump([2,0,2,3,1,3,1])