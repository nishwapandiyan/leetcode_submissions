from math import factorial
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        k -= 1
        nums = [str(i) for i in range(1,n+1)]
        for i in range(n,0,-1):
            fact = factorial(i-1)
            index = k // fact
            res.append(nums.pop(index))
            k %= fact
        return ''.join(res) 