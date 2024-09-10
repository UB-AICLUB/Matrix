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
          