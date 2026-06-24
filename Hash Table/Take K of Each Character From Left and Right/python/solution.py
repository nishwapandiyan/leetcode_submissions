class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if len(s) < 1:
            return -1
        elif k==0:
            return k    
        return len(s[k:len(s)-k])    