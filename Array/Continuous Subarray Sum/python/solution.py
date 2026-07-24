class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        store = {0:-1}
        rem = 0
        for i in range(len(nums)):
            rem += nums[i]
            rem %= k
            if rem not in store:
                store[rem] = i
            elif i - store[rem] >=2:
                return True
        return False        

        