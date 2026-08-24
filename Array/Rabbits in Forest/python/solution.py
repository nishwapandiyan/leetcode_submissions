class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans_freq = collections.Counter(answers)
        total = 0
        for ans,freq in ans_freq.items():
            group_size = ans + 1
            group = ceil(freq / group_size)
            total += group_size * group
        return total    