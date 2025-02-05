class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = []
        intervals.sort()
        for interval in intervals:
            if not n or n[-1][1] < interval[0]:
                n.append(interval)
            else:
                n[-1][1] = max(n[-1][1], interval[1])
        
        return n
# Time: O(n)
# Space: O(n)        
        