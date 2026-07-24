class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxval = 0
        chunks = 0

        for i in range(len(arr)):
            maxval = max(maxval,arr[i])

            if maxval ==  i:
                chunks += 1
        return chunks        