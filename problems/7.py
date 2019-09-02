class Solution:
	def reverse(self, x: int) -> int:
		if x < 0:
			ans = -int(str(-x)[::-1])
			if ans < -2147483648:
				return 0
		else:
			ans = int(str(x)[::-1])
			if ans > 2147483647:
				return 0
		return ans



x = 1534236469

print(Solution().reverse(x))