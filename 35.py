from typing import List

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		index = len(nums) // 2
		shift = index // 2
		while(True):
			if index > 0:
				if index == len(nums):
					return index
				if (nums[index] >= target and nums[index-1] < target):
					return index
				if nums[index] > target:
					index -= shift
				else:
					index += shift
			else:
				if nums[0] >= target:
					return 0
				else:
					return 1

			if shift > 0:
				shift = shift // 2
			else:
				shift = 1

		
x = [1,3,5,6]
target = 5

print(Solution().searchInsert(x, target))
