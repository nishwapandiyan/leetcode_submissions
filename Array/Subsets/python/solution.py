class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for elem in nums:
            res+= [curr + [elem] for curr in res]
        return res      