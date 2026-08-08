class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for ch in nums:
            d[ch] = d.get(ch,0)+1
        for k,v in d.items():
            if v > n // 2:
                return k