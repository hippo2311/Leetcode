class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for n in nums:
            if n in table:
                return True
            else:
                table.add(n)
        return False
# Time: O(n + m)
# Space: O(n)
