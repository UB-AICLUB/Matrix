from typing import List

class Matrix:
  def __init__(self,data:List):
    self.data = data
  
  # making a matrix of 0's of any size

  cols = int(input('enter the number of columns: '))
  rows = int(input('enter the number of rows: '))
  M = []
  for i in range(rows):
      M.append([])
      for j in range(cols):
          M[i].append(0)
