from typing import List

class Matrix:
  def __init__(self,data:List):
    self.data = data
  
  # making a matrix of 0's of any size
  def zeros(self,cols,rows):
    self.cols = cols
    self.rows = rows
    M = []
    for i in range(rows):
        M.append([])
        for j in range(cols):
            M[i].append(0)
    return(M)

  # creating an identity matrix of any size
  def identity(self,rowsId)
    Id = []
    self.rowsId = rowsId 
    for i in range(rowsId):
        Id.append([])
        for j in range(rowsId):
            Id[i].append(0)
            if i == j:
                Id[i][j] = 1
    return(Id)
