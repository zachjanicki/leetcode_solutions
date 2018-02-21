class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        sum = 0
        for i in range(len(nums)):
            if not i % 2:
                sum += nums_sorted[i]
        return sum
