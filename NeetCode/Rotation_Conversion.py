class Solution:
    def rotation_conversion(self, matrix):
        left = 0
        right = len(matrix) - 1
        top = left
        bottom = right

        while left < right:
            for i in range(right - left):
                temp = matrix[top][left + i]
                
                matrix[top][left + i] = matrix[top + i][right]          
                matrix[top + i][right] = matrix[bottom][right - i]      
                matrix[bottom][right - i] = matrix[bottom - i][left]    
                matrix[bottom - i][left] = temp                         
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix
            

if __name__ == '__main__':
    matrix = [[1, 2],[3, 4]]
    matrix = Solution.rotation_conversion(Solution, matrix)
    for x in matrix:
        print(x)

    """
    1  2
    3  4
    """