class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s

        i = 0
        res = [""] * len(s)
        backward = True

        for char in s:

            res[i] += char

            if i == 0 or i == numRows - 1:
                backward = not backward

            if backward:
                i -= 1
            else:
                i += 1

        return "".join(res)