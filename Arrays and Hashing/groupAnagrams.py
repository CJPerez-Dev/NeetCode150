"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
"""
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        string = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char)-ord("a")] += 1
            string[tuple(count)].append(s)

        return string.values()