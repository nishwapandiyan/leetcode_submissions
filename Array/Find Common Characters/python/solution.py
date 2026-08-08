from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c_ct = Counter(words[0])
        for word in words:
            c_ct &= Counter(word)
        res = list(c_ct.elements())
        return res        