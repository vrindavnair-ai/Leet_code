class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Legth of the list
        n = len(digits)

        #loop start at last index 
        for i in range (n-1,-1,-1):
            #if the digit is more than 9, adding 1 will bring carry
            #if digit is less than 9 add 1 and return the digits
            if digits[i]<9:
                #Add 1 to the last element
                digits[i] += 1
                #if digit is less than 9 return the digits and stop iterating
                return digits
            #If the digit is greater than 9 then the last digit will become 0
            digits[i] = 0
        return [1]+digits


        