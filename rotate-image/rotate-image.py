#Rotate a nxn 2D matrix representing an image

#Rotate the image by 90 deg 

#Modify the image directly (no additional 2D matrixes)

import math
from typing import List

class Solution:
   def rotate(self, matrix: List[List[int]]) -> None:
      """
      Matrix is modified, no returns
      """
      dict = {}
      rows = len(matrix)
      for c_rows in range(len(matrix)):
         for c_cols in range(len(matrix[c_rows])):
            n_rows = c_cols
            n_cols = rows - c_rows - 1
            val = matrix[c_rows][c_cols]
            dict[n_rows, n_cols] = val

      for key,val in dict.items():
         r,c = key
         matrix[r][c] = val