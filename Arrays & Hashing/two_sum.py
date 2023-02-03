def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Time Complexity: O(n)
        # Space Complexity: O(n)

        index_map = {}
        complement = 0

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in index_map:
                return [index_map.get(difference), i]
            index_map[nums[i]] = i
            
