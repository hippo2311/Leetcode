class Solution:
    def isValid(self, s: str) -> bool:
        table = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i not in table:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    peek = stack.pop()
                    if peek != table[i]:
                        return False
        return not stack
# Time: O(n)
# Space: O(n)

        