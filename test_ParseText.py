import unittest
import forTest

mat = ['0,0,1,1','0,0,1,1','1,1,0,0','1,1,0,0']
mat1 = ['0,1,0,1','0,1,0,1','1,0,1,0','1,0,1,0']
mat2 = ['0,1,0,0','1,0,1,1','0,1,1,0','1,1,1,0']
mat3 = ['0,0,1,1','0,0,1,1','1,1,0,0','1,1,0,0']
mat4 = ['0,1,1,1','1,0,1,1','1,1,0,1','1,1,1,0']

matrix = [mat, mat1, mat2, mat3, mat4]

matT = {1: [3, 4], 2: [3, 4], 3: [1, 2], 4: [1, 2]}
matT1 = {1: [2, 4], 2: [2, 4], 3: [1, 3], 4: [1, 3]}
matT2 = {1: [2], 2: [1, 3, 4], 3: [2, 3], 4: [1, 2, 3]}
matT3 = {1: [3, 4], 2: [3, 4], 3: [1, 2], 4: [1, 2]}
matT4 = {1:[2,3,4], 2:[1,3,4], 3:[1,2,4], 4:[1,2,3]}

matrixT = [matT, matT1, matT2, matT3, matT4]

class Test_test_1(unittest.TestCase):
    def test_A(self):
        i = 0
        k = 0
        while i < len(matrix):
            while k < len(matrix[i]):
                self.assertTrue(forTest.parseText(matrix[k]), matrixT[k])
                k += 1
            i += 1


if __name__ == '__main__':
    unittest.main()
