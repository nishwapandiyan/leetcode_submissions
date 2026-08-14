class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = set()
        for i in range(len(nums)):
            if i > k:
                w.remove(nums[i-k-1])
            if nums[i] in w:
                return True

            w.add(nums[i])
        return False            