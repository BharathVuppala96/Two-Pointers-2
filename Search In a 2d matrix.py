#Time complexity - 0(n+m) & space complexity - o(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix)==0:
            return False 
        m= len(matrix)
        n=len(matrix[0])
        row =0
        col = n-1

        while row<m and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col= col-1
            else:
                row = row+1
        return False 


    
        