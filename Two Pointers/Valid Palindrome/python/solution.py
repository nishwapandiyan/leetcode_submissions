class Solution:
    def isPalindrome(self, s: str) -> bool:
        # st = ""
        # for i in s:
        #     if i.isalnum():
        #         st+=i.lower()
        # l = 0
        # r = len(st)-1
        # while l<=r:
        #     if st[l] != st[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        new = ''.join(ch.lower() for ch in s if ch.isalnum())                
        if new != new[::-1]:
            return False
        return True    