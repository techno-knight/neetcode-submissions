class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return self.countCh(s) == self.countCh(t)

    def countCh(self,s):
        seek = {}

        for val in s:
            seek[val]= seek.get(val,0) + 1
        return seek