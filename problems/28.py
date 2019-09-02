from typing import List

class Solution:

	def prefix(self, s):
		v = [0]*len(s)
		for i in range(1,len(s)):
			k = v[i-1]
			while k > 0 and s[k] != s[i]:
				k = v[k-1]
			if s[k] == s[i]:
				k = k + 1
			v[i] = k
		return v
	
	def strStr(self, haystack: str, needle: str) -> int:
		if needle == "":
			return 0

		prefix = self.prefix(needle + "#" + haystack)
		n = len(needle)
		m = len(prefix)
		for i in range(n + 1, m):
			if prefix[i] == n:
				return i - n - n
		return -1
		
haystack = ""
needle = ""

print(Solution().strStr(haystack, needle))
