class Solution:
    def fib(self, n: int) -> int:
        a = {0:0, 1:1}
        def fibsum(x):
            if x in a:
                return a[x]
            else:
                a[x] = fibsum(x-1) + fibsum(x-2)
                return a[x]
    
        return fibsum(n)
        
# Time O(n)
# Space O(n)    