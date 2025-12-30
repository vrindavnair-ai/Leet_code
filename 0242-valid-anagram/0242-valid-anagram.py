class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create list of characters in s and t
        list_s = []
        list_t = []
        for i in s:
            list_s.append(i)
        list_s.sort()
        for i in t:
            list_t.append(i)
        list_t.sort()

        if list_s == list_t:
            return True
        else:
            return False

        