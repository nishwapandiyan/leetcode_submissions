class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
    
        res = []
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if sum(nums[i:j]) >= k:
                    return len(nums[i:j])
        return -1            