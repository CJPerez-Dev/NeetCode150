class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        for each in nums:
            if each in count:
                return True
            else:
                count[each] = 1
        return False
        