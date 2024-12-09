class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c] 
            else:
                counter[c] -= 1
        return True
# Time: O(n + m)
# Space: O(1)