class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        while k < len(arr):
            if abs(arr[-1]-x) >= abs(arr[0]-x):
                arr.pop()
            else:
                arr.pop(0)
            
        return arr
