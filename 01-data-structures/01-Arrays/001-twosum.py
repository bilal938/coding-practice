
def twoSum(self, nums, target):
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_d = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in num_d:
                return [num_d[comp], i]
            num_d[nums[i]]=i