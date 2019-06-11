def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        """implementing binary search: recursive, pick middle and range
        base case, when range = 1 i.e. left=right
        if left>right, search left, else right
        """
        def binSearch(lis, start, end):

            if start == end:
                return start

            mid = (start + end)/2
            if lis[mid] > lis[mid + 1]:
                return binSearch(nums, start, mid)
            return binSearch(nums, mid + 1, end)
        
        return binSearch(nums, 0, len(nums)-1)