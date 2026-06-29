class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        low = max(jobs)
        high = sum(jobs)

        while low < high:
            mid = low+(high-low)//2
            if canWork(mid):
                high = mid
            else:
                low = mid+1
        def canWork(limit):
            workers = [0]*k
            def dfs(index):
                
        return dfs(0)                     
