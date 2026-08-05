class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            res = ""
            if i ==0:
                lst.append(i)
            else:
                ct = 0
                while(i>0):
                    rem = i%2
                    res += str(rem)
                    i //= 2
                lst.append(res.count('1'))    

        return lst    