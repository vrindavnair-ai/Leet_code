class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        #length of string 
        s_len = len(s)
        #initialize value to 0
        value = 0
        #enumerate through each item
        for i in range(s_len):
            #if it is not the last value and the next value is more than current value
            if (i < s_len-1) and (num_dict[s[i]]<num_dict[s[i+1]]):
                #then subtract the current value
                    value -= num_dict[s[i]]
            else:
                #else add the current value to the value
                    value += num_dict[s[i]]
            

        return value

       
                




        