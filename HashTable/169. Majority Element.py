class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = -1
        count = 0
        for n in nums:
            if count == 0:
                maj = n
            if n == maj:
                count +=1
            else:
                count -= 1
        return maj

# Time: O(n)
# Space: O(1)
        