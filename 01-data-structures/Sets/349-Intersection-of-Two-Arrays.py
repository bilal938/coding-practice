class Solution:
"""
Given two arrays, write a function to compute their intersection.
Each element in the result must be unique.
The result can be in any order.
"""
    def set_intersection(self, set1, set2):
        return [i for i in set1 if i in set2]
        
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)