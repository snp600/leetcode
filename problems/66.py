from typing import List


class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		n = len(digits)
		for i in range(1, n+1):
			if digits[n-i] != 9:
				digits[n-i] += 1
				break
			else:
				digits[n-i] = 0
		if digits[0] == 0:
			return [1] + [0] * n
		return digits


n = [9,9,9]

print(Solution().plusOne(n))