class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        for k,v in d.items():
            if v == 1:
                return k    