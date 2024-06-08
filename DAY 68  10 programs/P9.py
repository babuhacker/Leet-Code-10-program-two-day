# Sqrt(X)

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        result = 0

        while l <= r:
            m = l +((r-1) // 2)
            if m**2 > x:
                r = m- 1
            elif m**2 < x:
                l = m + 1
                result = m
            else:
                return m
        return result
