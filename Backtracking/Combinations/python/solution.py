from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        op = list(range(1,n+1))
        res = [x for x in combinations(op,k)]
        return res