class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total, tank, start = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1
