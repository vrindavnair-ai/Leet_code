class Solution:
    def canWinNim(self, n: int) -> bool:
        """ 
        case n =1 -> you win
        case n =2 -> you win
        case n =3 -> you win
        case n =4 -> friend win (even if you take 1 ,2, or 3 in the initial turn, the remaining will be less than 3)
        case n =5 -> you win if you take 1 initially (makes 4 remaining which is loss position for your friend)
        case n =6 -> you win if you take 2 initially (makes 4 remaining which is loss position for your friend)
        case n =7 -> you win if you take 3 initially (makes 4 remaining which is loss position for your friend)
        case n =8 -> friend win (even if you take 1,2 or 3 that makes 7,6,5 for your friend which is lossing position for him)
        case n =9 -> you win (if you take 1 it will make it 8 for your friend which is loss position for your friend)
        
        --> The cycle continues
        --> you will loss if n is multiple of 4
        """
        if n%4 == 0:
            return False

        return True

        