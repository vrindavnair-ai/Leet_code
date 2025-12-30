class Solution:
    def isHappy(self, n: int) -> bool:
        #The function to calculate sum of squares of each number
        def sq_dits(number):
            #variable to store sum
            sm_sq = 0
            #Iterate throgh each digit
            while number>0:
                #to get the last digit
                #suppose number is 282 it fetch 2
                digit = number % 10
                #square of digit and add it to sum
                sm_sq += digit*digit
                #Remove the last digit from number
                #suppose number is 282 it fetch 28
                number = number // 10
            return sm_sq

        #create a set to store the sqared sum to check if it already exists
        set_sum = set()
        #Iterate this loop only if the number is not 1
        #and the number is already in sqared sum set (to reject the situation where it run through endlesslly)
        while n!=1 and n not in set_sum:
            #Update the set with numbers
            set_sum.add(n)
            sqr_digt = sq_dits(n)
            #update n to new value of sum of squared digits
            n = sqr_digt


        if n == 1:
            return True
        else :
            return False



        