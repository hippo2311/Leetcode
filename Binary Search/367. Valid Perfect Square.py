class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L = 1
        R = num
        while L <= R:
            mid = (L+R)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                L = mid + 1
            else:
                R = mid - 1
        return False
# Time O(logn)
# Sapce O(1)