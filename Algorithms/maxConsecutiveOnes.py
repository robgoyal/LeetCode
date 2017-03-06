class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tmpOnes = 0
        maxOnes = []

        for i in range(len(nums)):
            if nums[i] == 1:
                tmpOnes += 1

            else:
                maxOnes.append(tmpOnes)
                tmpOnes = 0

        # Case where theres only one element or 1 is at the end of the list
        maxOnes.append(tmpOnes)
        return max(maxOnes)
