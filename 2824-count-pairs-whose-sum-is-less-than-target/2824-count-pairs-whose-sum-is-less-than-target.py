class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        length = len(nums)
        count = 0
        #every pair (i, j) where i < j and count if nums[i] + nums[j] < target.
        for i in range (length):
            for j in range (i+1, length):
                if (nums[i]+nums[j]<target):
                    count = count+1

        return count
        