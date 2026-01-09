class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #define a set
        #set will take unique values only
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        #use the intersection
        nums3_set = nums1_set.intersection(nums2_set)
        #convert it back to list
        nums3 = list(nums3_set)
        print(nums3)
        return nums3