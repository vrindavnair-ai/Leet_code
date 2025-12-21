class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #initialize a new array to store square
        length_arr = len(nums)
        new_array = [0]*length_arr
        #Since the array is already sorted we just have to check absolute value of left and right values
        #it helps in sorting the new array in effective way
        left_idx = 0
        right_idx = length_arr-1
        #filling the new array in sorted order
        #start filling from the last element in descending order until the 0th index(that's why we have -1)
        #because the edge values will have greater values
        for i in range (length_arr-1,-1,-1):
            if (abs(nums[left_idx])>abs(nums[right_idx])):
                new_array[i] = nums[left_idx]**2
                left_idx += 1

            else:
                new_array[i] = nums[right_idx]**2
                right_idx -= 1

        return new_array

        

            
        