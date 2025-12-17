class Solution:
    def climbStairs(self, n: int) -> int:
        #n_ways = 1
        if n <= 2:
            return n

        first = 1
        second = 2
        for i in range (3, n+1):
            n_ways = first+second
            first = second
            second = n_ways

        return n_ways
"""
* Step 1 (n=1) - > 1 way: [1]
* Step 2 (n=2) -> 2 ways: [1, 1], [2]
* Step 3 (n=3) -> You can reach Step 3 from Step 2 (2 ways) OR Step 1 (1 way).
    * 2 + 1 = 3 ways.
    * Paths: [1,1,1], [2,1], [1,2]
* Step 4 (n=4) -> You can reach Step 4 from Step 3 (3 ways) OR Step 2 (2 ways).
    * 3 + 2 = 5 ways.
* Step 5 (n=5):
    * Reachable from Step 4 (5 ways) or Step 3 (3 ways).
    * 5 + 3 = 8 ways.
If you look at the results (1, 2, 3, 5, 8...), this is exactly the Fibonacci sequence."""

        

        




        