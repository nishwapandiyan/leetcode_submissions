class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        st = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                if st == nums[i-1]:
                    res.append(str(st))
                else:
                    res.append(str(st)+"->"+str(nums[i-1]))
                st = nums[i]
        if st == nums[-1]:
            res.append(str(st)) 
        else:
            res.append(str(st)+"->"+str(nums[i])) 
        return res                      
