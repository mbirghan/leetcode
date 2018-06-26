class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if(numRows == 0):
            return []
        
        currentRow = [1]
        returnList = []
        
        returnList.append(currentRow)
        
        for i in range(1,numRows):
            returnList.append(self.generateRow(currentRow))
            currentRow = returnList[-1]
            
        return returnList
        
        
    def generateRow(self, prevRow):
        newRow = [1] * (len(prevRow)+1)
        for i in range(0, len(prevRow)-1):
            newRow[i+1] = prevRow[i] + prevRow[i+1]
        return newRow