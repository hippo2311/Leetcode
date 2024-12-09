class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range (len(nums)):
            h[nums[i]] = i
        for i in range (len(nums)):
            value = target - nums[i]

            if value in h and h[value] != i:
                return [i, h[value]]


# Time Complexity: O(n)
# Space Complexity: O(n)