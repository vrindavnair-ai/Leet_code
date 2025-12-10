class Solution:
    def isValid(self, s: str) -> bool:
        #to store parenthesis
        par_list = []
        #to store open close parenthesis as a dictionary
        par_dict = {")":"(","}":"{","]":"["}
        
        for ch in s:
            if ch in par_dict.keys():
                if par_list == []:
                #if the list is empty the closing bracket is the first element
                    return False
                #to check if the last element match corresponding closing bracket
                elif par_dict[ch] == par_list[-1]:
                    par_list.pop()
                else:
                    return False
            else:
                par_list.append(ch)

        if par_list == []:
            return True
        return False


                
        