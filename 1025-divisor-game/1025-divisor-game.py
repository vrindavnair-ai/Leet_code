class Solution:
    def divisorGame(self, n: int) -> bool:
       # if the starting number is even alice wins and if it is odd alice fails
         if n % 2 == 0:
            return True
         return False
        