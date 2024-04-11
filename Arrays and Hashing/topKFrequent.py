"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        elements = {}
        result = []

        for num in nums:
            elements[num] = elements.get(num, 0) + 1
        sort = sorted(elements.items(), key=lambda x: x[1], reverse=True)

        for i, (key, value) in enumerate(sort):
            if i < k:
                result.append(key)
        return result