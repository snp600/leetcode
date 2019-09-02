class Solution:
	def titleToNumber(self, s: str) -> int:
		n = len(s)
		ans = 0
		for i in range(n):
			ans += (ord(s[n - i - 1]) - 64) * (26 ** i)
		return ans
	

s = "BA"

print(Solution().titleToNumber(s))
