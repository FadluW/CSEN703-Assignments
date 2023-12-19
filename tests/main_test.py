# Import libraries
import numpy as np
import unittest

from ScoringMatrix import ScoringMatrix

class TestScoringMatrix(unittest.TestCase):

    def test_scoringMatrixScores(self):
        matrixArr = [[1, -0.8, -0.2, -2.3, -0.6],
                    [-0.8, 1, -1.1, -0.7, -1.5],
                    [-0.2, -1.1, 1, -0.5, -0.9],
                    [-2.3, -0.7, -0.5, 1, -1],
                    [-0.6, -1.5, -0.9, -1, 0]]
        scoringMatrix = np.array(matrixArr)
        scoringMatrix2 = ScoringMatrix(scoringMatrix)

        self.assertEqual(scoringMatrix2.getScore('A', 'T'), -0.2)
        self.assertEqual(scoringMatrix2.getScore('DASH', 'T'), -0.9)

if __name__ == '__main__':
    unittest.main()