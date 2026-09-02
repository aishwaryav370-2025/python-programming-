class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash_map = dict()
        
        for index, val in enumerate(nums):
            if hash_map.has_key(val):
                return [hash_map.get(val), index]

            hash_map[target - val] = index
