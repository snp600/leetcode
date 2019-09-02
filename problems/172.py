from typing import List


class Solution:
    def trailingZeroes(self, n: int) -> int:
    	ans = 0
    	mul = 5
    	while(mul <= n):
    		ans += n//mul
    		mul *= 5
    	return ans

n = 5

print(Solution().trailingZeroes(n))
