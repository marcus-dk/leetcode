"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""

# intuition notes:
# originally i forgot that i was supposed to be efficient, so i sorted and proceeded to pop from each end until i find the middle
# then i laughed and figured, if list len is even, the two middle nums summed div 2 is the median, if it's odd, its the middle value

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)

        if len(nums1)%2==0:
            return (sorted(nums1)[len(nums1)//2-1:len(nums1)//2][0] + sorted(nums1)[len(nums1)//2:len(nums1)//2+1][0]) / 2
            # returns the lower of the middle + upper of the middle / 2
        return sorted(nums1)[len(nums1)//2]
        
# solution noteS:
# pirated the idea, took no time at all, 87ms beats 87.88%, 16.65MB beats 41.06%
# so it's kinda fast, and dogshit memory wise. i realise it can be solved via binary search, i'm just not smart enough for that yet