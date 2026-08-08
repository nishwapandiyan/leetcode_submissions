class Solution:
    def maxDifference(self, s: str) -> int:
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0)+1
        max_odd = 0
        min_even = float("inf")
        for v in d.values():
            if v %2 != 0:
                max_odd = max(max_odd,v)
            else:
                min_even = min(min_even,v) 
        return max_odd - min_even         