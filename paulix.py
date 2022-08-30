
from qoperators import SingleQuBitOperator
import numpy as np


class PauliX(SingleQuBitOperator):

    # PauliX operator matrix is input into the SingleQuBitOperator parent class constructor
    def __init__(self):
        super().__init__(np.array([[0, 1], [1, 0]]))
