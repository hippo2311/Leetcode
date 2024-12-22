class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        max_avg = cur_sum / k
        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]
            avg = cur_sum / k
            if avg > max_avg:
                max_avg = avg
        return max_avg
# Time: O(n)
# Space: O(1)