class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(t)
        counter1 = Counter(s)
        if len(s)!= len(t):
            return False
        return counter == counter1
# Time: O(n)
# Space: O(n)