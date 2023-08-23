"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""

# 23/08/2023 during Danish Lesson. Marcus Sorensen

# intuition notes:
# sort word chars alphabetically, match to dict if new append new item, if match append to value, when done, return list of anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for word in strs:
            alphword = ''.join(sorted(list(word)))
            if alphword in anagrams:
                anagrams[alphword].append(word)
            else:
                anagrams[alphword]=[word]   
        
        return [value for key,value in anagrams.items()]  
        

# solved in about 15-20 mins, Runtime 90ms beats 95.74%, Memory 19.62 MB beats 75.24%
# Python3
