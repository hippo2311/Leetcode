class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        for i in range(len(s)):
            # Check if this numeral is smaller than the next one
            if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
                total -= d[s[i]]  # Subtract this numeral
            else:
                total += d[s[i]]  # Add this numeral
        return total
# Time Complexity: O(N)
# Space Complexity: O(1)