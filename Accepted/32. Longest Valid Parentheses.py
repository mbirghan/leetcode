class Solution(object):
    def getMax(self, lvlStart, lvlEnd):
        best = -1
        bestLength = 0

        for i in range(0,len(lvlStart)):
            if(lvlStart[i] >= 0 and lvlEnd[i] >= 0):
                if(bestLength <= (lvlEnd[i]-lvlStart[i]+1)):
                    best = i
                    bestLength = lvlEnd[i]-lvlStart[i]+1
        return bestLength

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        lvlStart = []
        lvlEnd = []
        lvl = 0
        bestTilNow = 0

        for i in range(0, len(s)):

            if(s[i] == "("):
                lvl += 1
                if(len(lvlStart) < lvl):
                    lvlStart.append(i)
                    lvlEnd.append(-1)

            if(s[i] == ")"):
                if(lvl <= 0):
                    bestToTest = self.getMax(lvlStart, lvlEnd)
                    if(bestTilNow < bestToTest):
                        bestTilNow = bestToTest
                    lvlStart = []
                    lvlEnd = []
                    continue
                lvl -= 1
                lvlEnd[lvl] = i
                lvlStart = lvlStart[:lvl+1]
                lvlEnd = lvlEnd[:lvl+1]

        bestToTest = self.getMax(lvlStart, lvlEnd)
        if(bestTilNow < bestToTest):
            bestTilNow = bestToTest

        return bestTilNow

s = Solution()
print(s.longestValidParentheses("()(()"))

        # levelStack = []

        # wasValid = False
        # current = (0,-1,-1)

        # for i in range(0, len(s)):
        #     valid = wasValid
        #     wasValid = False
        #     if(s[i] == "("):
        #         levelStack.append(i)

        #     if(s[i] == ")"):
        #         if(len(levelStack) > 0):
        #             wasValid = True
        #             counterpart = levelStack.pop()
        #             if(i-counterpart+1 > best):
        #                 best = i-counterpart+1
        #                 start = counterpart
        #                 end = i
        #             elif():


        # return best
