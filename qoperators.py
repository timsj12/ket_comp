
import numpy as np
from qbit import Qbit


class InvalidOperator(Exception):
    pass


class SingleQuBitOperator:

    # class constructor requiring matrix input
    def __init__(self, operator_matrix):
        self.operator_matrix = operator_matrix

    # operation matrix performed on qubit
    def operate(self, qubit):
        zero = np.dot(self.operator_matrix, qubit.alpha * np.array([1, 0]))
        one = np.dot(self.operator_matrix, qubit.beta * np.array([0, 1]))

        # sum of zero and one states from dot product is the new qbit state
        zero_state = zero[0] + one[0]
        one_state = zero[1] + one[1]

        # new qubit object created and returned
        qubit = Qbit(zero_state, one_state)

        return qubit
