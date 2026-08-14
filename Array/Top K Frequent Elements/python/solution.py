class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for c in nums:
            d[c] = d.get(c,0)+1
        bucket = [[] for _ in range(len(nums)+1)]

        for key,val in d.items():
            bucket[val].append(key)
        res = []
        for pos in range(len(bucket)-1,0,-1):
            for n in bucket[pos]:
                res.append(n)

                if len(res) == k:
                    return res
        return res            