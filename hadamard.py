
from qoperators import SingleQuBitOperator
import numpy as np
import math


class Hadamard(SingleQuBitOperator):

    # Hadamard operator matrix is input into the SingleQuBitOperator parent class constructor
    def __init__(self):
        super().__init__((1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]]))
