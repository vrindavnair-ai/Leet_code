class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a dictionary to store each string and corresponding character set
        str_dict = {}
        #iterate through each word in the list of strings
        for i in strs:
            #Create a list to store the characters in the word
            str_list = []
            #iterate throgh each character in the word
            for j in i:
                str_list.append(j)
            str_list.sort()

            #print(list(str_dict.keys()))
            #convert the list to tuple to use it as a key (list can't be used as key because it is mutable)
            str_tuple = tuple(str_list)

            if str_tuple not in list(str_dict.keys()):
                str_dict[str_tuple] = [i]
            else:
                str_dict[str_tuple].append(i)
        
        result  = list(str_dict.values())
        print(result)

        return result
