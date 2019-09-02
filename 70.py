class Solution:
	def factorial(self, k):
		fact = 1
		for i in range(k):
			fact *= (i + 1)
		return fact

	def cnk(self, n, k):
		ans = 1
		for i in range(k):
			ans *= (n-i)
		return ans / self.factorial(k)

	def climbStairs(self, n: int) -> int:
		ans = 0
		for i in range(n//2 + 1):
			cells = n - i
			ans += self.cnk(cells, i)
		return int(ans)

n = 7

print(Solution().climbStairs(n))
