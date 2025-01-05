class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:0, 1:1, 2:2}
        def f(a):
            if a in memo:
                return memo[a]
            else:
                memo[a] = f(a-1) + f(a-2)
                return memo[a]
        return f(n)
# Time O(n)
# Space O(n)   