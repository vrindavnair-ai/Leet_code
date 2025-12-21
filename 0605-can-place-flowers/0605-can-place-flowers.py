class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if (length == 1): 
            if(flowerbed[0]==0 and n!=0):
                 n = n-1
                 flowerbed[0] = 1
        else:
            for i in range(0,length):
                if(n!=0):
                    if(i==0):
                        if (flowerbed[i]==0 and flowerbed[i+1]==0):
                            n = n-1
                            flowerbed[i] = 1
                    elif (i==(length-1)):
                        if (flowerbed[i]==0 and flowerbed[i-1]==0):
                            n = n-1
                            flowerbed[i] = 1

                    else:
                 #checking if the previous and next flower bed is empty
            #plant until we reach the target n (n==0)
                        if(flowerbed[i-1]==0 and flowerbed[i] ==0 and flowerbed[i+1]==0):
                            n = n-1
                #if the condition is true. the plot is planted 
                            flowerbed[i] = 1
                else:
                    return True

        if n == 0:
            return True

        else:
            return False

        
        