# TC: O(m*n) where m and n are the rows and cols of the matrix
#SC: O(1) because we are appending the nums to the result array which we are returning.
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # optimized

        res = []
        r = 0

        while True:

            if r < len(mat):
                c = 0
            else:
                r -= 1
                c+=1

            if c == len(mat[0]):
                break

            i = r
            j = c
            temp = []
            while i >= 0 and j < len(mat[0]):
                temp.append(mat[i][j])
                i-=1
                j += 1

            if (r+c) % 2 == 0:
                res.extend(temp)
            else:
                res.extend(temp[::-1])

            r +=1
        
        return res