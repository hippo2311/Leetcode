class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = 0, 0
        r = []
        for i in range(max(len(word1), len(word2))):
            if a < len(word1):
                r.append(word1[a])
                a += 1
            if b < len(word2):
                r.append(word2[b])
                b += 1
        return "".join(r)

# Time Complexity O(n)
# Space Complexitu O(1)