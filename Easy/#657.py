class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        movesDict = {"L":0, "R":0, "D":0, "U":0}
        for i in range(len(moves)):
            movesDict[moves[i]] += 1
            
        if(movesDict["L"] == movesDict["R"] and movesDict["D"] == movesDict["U"]):
            return True 
        return False 
