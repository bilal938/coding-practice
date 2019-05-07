class Solution(object):
    def nextPermutation(self, nums):
        """
        Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

        If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

        The replacement must be in-place and use only constant extra memory.

        Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

        1,2,3 → 1,3,2
        3,2,1 → 1,2,3
        1,1,5 → 1,5,1
        
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(n, i, j):
            temp = n[i]
            n[i] = n[j]
            n[j] = temp

        def reverse(n, i):
            j = len(n) - 1
            while i < j:
                swap(n,i,j)
                i += 1
                j -= 1
        
        i = len(nums) - 2
        
        while nums[i+1] <= nums[i] and i >= 0:
            i -= 1
            
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            swap(nums, i, j)
        
        reverse(nums, i + 1)
        
    
                
        