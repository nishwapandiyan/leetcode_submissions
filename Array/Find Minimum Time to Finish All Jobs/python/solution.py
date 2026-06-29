class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        if k == n:
          return max(jobs)
        else:
            maxx = 0
            for i in range(n-1):
                cur = jobs[i] + jobs[i+k-1]
                if cur <= n*2 + 1:
                  maxx = max(maxx,cur)
        return maxx        
