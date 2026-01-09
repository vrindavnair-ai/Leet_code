class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #find length of both strings
        ransomNote_len  = len(ransomNote)
        magazine_len = len(magazine)
        
        #if the length of Ransom note is more we can't create it using Magazine
        if ransomNote_len>magazine_len:
            return False
        
        else:
            #make Magazine to a dictionary with character and the number of each characters
            magazine_dict = {}
            for i in magazine:
                #if the character is not in dictionary key add new dictionary key
                if i not in magazine_dict.keys():
                    magazine_dict[i] = 1
                #if the ke is there in dictionary increase the value by 1
                else:
                   new_value = magazine_dict[i]+1
                   magazine_dict[i] = new_value
            #check each character in ransomNote against the keys in magazine_dict
            for i in ransomNote:
                #if the charecter is not in keys. ransomNote can't be constructed using magazine
                if i not in magazine_dict.keys():
                    return False
                #if the key is present decrement the value by 1
                else:
                    #If the value is 0 return False
                    if(magazine_dict[i]==0):
                        return False
                    else:
                        new_value = magazine_dict[i]-1
                        magazine_dict[i] = new_value
            return True
