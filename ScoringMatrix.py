import numpy as np
from enum import Enum

class Gene(Enum):
    A = 0
    G = 1
    T = 2
    C = 3
    DASH = 4


class ScoringMatrix:
    def __init__(self, matrix: np.ndarray):
        self.matrix = matrix

    def getScore(self, x: chr, y: chr):
        return self.matrix[Gene[x].value][Gene[y].value]