import unittest
import forTest

answer = [1, 3, 2, 4]
answer1 = [1, 2, 4, 3]
answer2 = [1, 3, 2, 4]
answer3 = None
answer4 = None

masAns = [answer, answer1, answer2, answer3, answer4]

input = {1: [3, 4], 2: [3, 4], 3: [1, 2], 4: [1, 2]}
input1 = {1: [2, 4], 2: [2, 4], 3: [1, 3], 4: [1, 3]}
input2 = {1: [3, 4], 2: [3, 4], 3: [1, 2], 4: [1, 2]}
input3 = {1:[0], 2:[1], 4:[3]}
input4 = {1:[3], 2:[2], 4:[1]}

masIn = [input, input1, input2, input3, input4]


class Test_test_Hamiltonov(unittest.TestCase):
    def test_A(self):
        i = 0
        while i < len(masAns):
            tmp = forTest.hamilton(masIn[i], len(masIn[i]), 1)
            ans = str(tmp).strip(';')
            self.assertTrue(ans, masAns[i])
            i += 1

if __name__ == '__main__':
    unittest.main()
