class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        def subset(start,current):
            res.append(current[:])
            for i in range(start,len(nums)):
                
                if i > start and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])

                subset(i+1,current)

                current.pop()
        subset(0,[])
        return res        