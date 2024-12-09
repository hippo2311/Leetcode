class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0 
        table = set(jewels)

        for stone in stones:
            if stone in table:
                count += 1
        return count
        
# Time: O(n + m)
# Space: O(n)