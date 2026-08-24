class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        max_num = max(arr1)
        frq = [0] * (max_num + 1)
        for num in arr1:
            frq[num] += 1
        for num in arr2:
            res.extend([num] * frq[num])
            frq[num] = 0
        for num in range(max_num+1):
            res.extend([num]*frq[num])
        return res       