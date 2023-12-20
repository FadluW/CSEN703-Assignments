# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import random
import time
from ScoringMatrix import ScoringMatrix

def main():
    plot = False
    if (plot): return testPlot()

    seq1 = "ATGCC"
    seq2 = "TACGCA"
    matrixArr = [[1, -0.8, -0.2, -2.3, -0.6],
                 [-0.8, 1, -1.1, -0.7, -1.5],
                 [-0.2, -1.1, 1, -0.5, -0.9],
                 [-2.3, -0.7, -0.5, 1, -1],
                 [-0.6, -1.5, -0.9, -1, 0]]
    scoringMatrix = np.array(matrixArr)

    sequenceAlignment(seq1, seq2, scoringMatrix, True)


def validateScoringMatrix(matrix: np.ndarray):
    # Ensure scoring matrix is of size 5x5
    if (matrix.ndim != 2 or matrix.shape != (5, 5)): return False

    return True


def sequenceAlignment(seq1: str, seq2: str, scoring: np.ndarray, printing: bool):
    if (not validateScoringMatrix(scoring)):
        printing("Invalid Scoring Matrix")
        return
    
    # Keep seq1 as the longer one
    if (len(seq2) > len(seq1)):
        temp = seq1
        seq1 = seq2
        seq2 = temp

    if printing: printStart(seq1, seq2, scoring)

    scoringMatrix = ScoringMatrix(scoring)
    
    m = len(seq1)
    n = len(seq2)

    # Initialize sequence alignment score table to memorize in
    SAS = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        SAS[i][0] = scoringMatrix.getScore(seq1[i - 1], "DASH")

    for j in range(1, n + 1):
        SAS[0][j] = scoringMatrix.getScore(seq2[j - 1], "DASH")

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_score = scoringMatrix.getScore(seq1[i - 1], seq2[j - 1])

            SAS[i][j] = max(
                round(SAS[i - 1][j - 1] + match_score, 1),  # Match or mismatch
                round(SAS[i - 1][j] + scoringMatrix.getScore(seq1[i - 1], "DASH"), 1),  # Gap in sequence 2
                round(SAS[i][j - 1] + scoringMatrix.getScore("DASH", seq2[j - 1]), 1)  # Gap in sequence 1
            )

    if printing: 
        printEnd(SAS[m][n])
        print(np.array(SAS))
    return SAS[m][n]


def printStart(seq1: str, seq2: str, scoring: np.ndarray):
    print("==============================\n\n")
    print("Starting Sequence Alignment for:")
    print("\nSeq1: ", seq1, "\nSeq2: ", seq2)
    print("\nScoring Matrix: \n", scoring, "\n\n")


def printEnd(score):
    print("\nAlignment found with score: ", score)
    print("\n\n==============================\n")


def generateSequence(length: int):
    seq = [randChar() * length]
    return ''.join(seq)


def randChar():
    return "AGTC"[random.randint(0, 3)]


def testPlot():
    matrixArr = [[1, -0.8, -0.2, -2.3, -0.6],
                 [-0.8, 1, -1.1, -0.7, -1.5],
                 [-0.2, -1.1, 1, -0.5, -0.9],
                 [-2.3, -0.7, -0.5, 1, -1],
                 [-0.6, -1.5, -0.9, -1, 0]]
    scoringMatrix = np.array(matrixArr)
    
    ax = plt.subplot()
    for i in range(10, 100):
        seq1 = generateSequence(i)
        for j in range(10, 20):
            seq2 = generateSequence(j)
            
            startTime = time.time()
            sequenceAlignment(seq1, seq2, scoringMatrix, False)
            timeElapsed = time.time() - startTime

            ax.scatter(i * j, timeElapsed)
    
    plt.show()


if __name__ == "__main__":
    main()