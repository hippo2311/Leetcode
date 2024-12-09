class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -=1
                continue
            if s[right].lower() != s[left].lower():
                return False
            
            left += 1
            right -= 1
        return True
        
# Time: O(n)
# Space: O(1)
        