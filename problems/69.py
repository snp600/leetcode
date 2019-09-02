from typing import List



class Solution:
	def mySqrt(self, x: int) -> int:
		if x == 0:
			return 0
		eps = 0.0001
		a = 1
		flag = False
		while True:
			b = (a + x // a) >> 1
			if (a == b or b > a and flag == True):
				break
			flag = b < a
			a = b
		return a

x = 0

print(Solution().mySqrt(x))
