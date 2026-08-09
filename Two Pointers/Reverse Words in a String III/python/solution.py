class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        r = s.split(" ")
        for ch in  r:
            res += ch[::-1]+" "
        return res.strip()    

