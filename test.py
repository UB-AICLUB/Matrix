import unittest

from matrix import Matrix

# write your test cases here
class TestMatrix(unittest.TestCase):
  def test_shape(self):
    m1 = Matrix([
      [1,2,3],
      [4,5,6],
    ])
    m2 = Matrix(
      [
        [    
          [1,2,3],
          [4,5,6],
        ],
        [    
          [1,2,3],
          [4,5,6],
        ]
      ]
    )
    # add more test cases if you feel like!
    self.assertEqual(m1.shape(),(2,3))
    self.assertEqual(m2.shape(),(2,2,3))

if __name__ == '__main__':
    unittest.main()
