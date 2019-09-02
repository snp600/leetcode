from typing import List


class Solution:
	def sumOfSquares(self, n: int) -> int:
		ans = 0
		while(n != 0):
			ans += (n % 10)**2
			n //= 10
		return ans

	def isHappy(self, n: int) -> bool:
		for _ in range(100):
			n = self.sumOfSquares(n)
			if n == 1:
				return True
		return False

n = 19

#print(Solution().sumOfSquares(n))
print(Solution().isHappy(n))
