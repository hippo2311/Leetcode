class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom Up DP (Constant Space)
        n = len(cost)
        prev, curr = 0, 0

        for i in range(2, n+1):
            prev, curr = curr, min(cost[i-2] + prev, cost[i-1] + curr)
        
        return curr

        # Time: O(n)
        # Space: O(1)
        