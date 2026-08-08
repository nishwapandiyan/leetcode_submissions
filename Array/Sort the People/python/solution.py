class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for n,h in zip(names,heights):
            d[h] = n
        res = []    
        for c in reversed(sorted(heights)):
            res.append(d[c])    
        return res    