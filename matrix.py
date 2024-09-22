from typing import List

class Matrix:
  def __init__(self,data:List):
    """
    Initialize a matrix with the provided data.
    """
    self.data = data

  def __str__(self):
    """
    Return a string representation of the matrix.
    """
    output_str_matrix = ""
    for row in self.data:
      output_str_matrix += str(row) + "\n"
    return output_str_matrix

  def shape(self):
    """
    Return the shape of the matrix as a tuple. If the matrix is not valid, return None.
    """
    if self.data == None:
      return None
    else:
      size = ()
      matrix = self.data
      while True:
        if type(matrix) == list:
          size = size + (len(matrix),)
          if type(matrix[0]) == int:
            return size
          matrix = matrix[0]
  
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

  def transpose(self,A):
    self.A = A
    cols = len(self.A[0])
    rows = len(self.A)
    T = []
    for i in range(cols):
        T.append([])
        for j in range(rows):
            T[i].append(0)
    for i in range(cols):
        for j in range(rows):
            T[i][j] = A[j][i]
    return(T)

  def multiply(self,A,B):
    mOutput = []
    self.A = A
    self.B = B
    outCol = len(B[0])
    outRow = len(A)
    commonLen = len(A[0])
    for i in range(outRow):
        mOutput.append([])
        for j in range(outCol):
            mOutput[i].append(0)

    for k in range(commonLen):
        for i in range(outRow):
            for j in range(outCol):
                mOutput[i][j] += (A[i][k]*B[k][j])

    return(mOutput)
