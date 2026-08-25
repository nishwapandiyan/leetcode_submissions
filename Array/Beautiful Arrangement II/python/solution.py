class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        nums = [x for x in range(1,n-k+1)]
        dr = 1
        diff = k
        for _ in range(k):
            nums.append(nums[-1]+(dr*diff))
            dr *= -1
            diff -= 1
        return nums    