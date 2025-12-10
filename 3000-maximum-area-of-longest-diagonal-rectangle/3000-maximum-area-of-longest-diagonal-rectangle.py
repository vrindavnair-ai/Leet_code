class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_dig_sqr = 0
        max_sqr_area = 0
        #print(dimensions)

        for l,w in dimensions:
            diag_sqr = (l*l)+(w*w)
            sqr_area = l*w
            if diag_sqr > max_dig_sqr :
                max_sqr_area = sqr_area
                max_dig_sqr = diag_sqr
                
            elif diag_sqr == max_dig_sqr and sqr_area > max_sqr_area:
        #if multiple restangle with same diagonal sqaure use one with greater area
                max_sqr_area = sqr_area
                    

        return max_sqr_area



        