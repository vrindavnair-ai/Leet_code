class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        length = len(s)
        #dictionary to store characters
        char_dict = {} #to store count of each number
        max_length = 0
        left_idx = 0 #starting index of substring to be counted 

        for i in range(length):
            #increment the count of character in character dictionary
            #.get function return 0 if the character is not already in the dictionary
            char_dict[s[i]] = char_dict.get(s[i],0)+1

            #if any character count increases above 2 change the start of substring to next position
            #reduce the count of charcter as substring moves
            while (char_dict[s[i]]>2):
                char_dict[s[left_idx]] = char_dict[s[left_idx]] -1
                left_idx = left_idx+1

            #update the maxlength
            #check if the current string is larger than previous substring
            max_length = max(max_length, i-left_idx+1)

        return max_length


        