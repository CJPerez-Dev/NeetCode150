"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        string1 = {}
        string2 = {}
        
        for each in s:
            string1[each] = string1.get(each, 0) + 1
        for each in t:
            string2[each] = string2.get(each, 0) + 1

        if string1 == string2:
            return True
        return False
        