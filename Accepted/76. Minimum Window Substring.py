class Solution:
    def minWindow(self, s, t):
        alphabetMap = {}
        nxt = []
        left = 0
        right = 0
        leftBest = -1
        rightBest = len(s)
        uniqueCharacters = 0
        uniqueCharactersFound = 0

        for i in t:
            if(i in alphabetMap):
                alphabetMap[i] += 1
            else:
                alphabetMap[i] = 1
                uniqueCharacters += 1


        for index in range(0, len(s)):
            if(s[index] in alphabetMap):
                nxt.append(index)
                alphabetMap[s[index]] -= 1
                right = index

                if(alphabetMap[s[index]] == 0):
                    uniqueCharactersFound += 1
            
                while s[nxt[0]] in alphabetMap and alphabetMap[s[nxt[0]]] < 0:
                    alphabetMap[s[nxt[0]]] += 1
                    nxt.pop(0)
                    
                if(uniqueCharacters == uniqueCharactersFound):
                    if(abs(nxt[0]-right) < abs(leftBest-rightBest)):
                        leftBest = nxt[0]
                        rightBest = right

        for i in t:
            if(alphabetMap[i] > 0):
                return ""

        return s[leftBest:rightBest+1]

            