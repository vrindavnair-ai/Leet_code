class Solution:
    def removeDuplicates(self, s: str) -> str:
        #define an empty list
        s_list = []
        #iterate over the string to get each character
        for i in s:
            #check if list is empty. if it is empty it won't calculate next condition(short circuit evaluation)
            #if not check the last value in list is same as the current character in string
            if s_list and s_list[-1]==i:
                #to remove the last character
                s_list.pop() 
            else:
                s_list.append(i)
        return "".join(s_list)
