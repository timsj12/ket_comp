# Tim Jarvis
# Final Exam: Quantum Computation
# Due Date: August 23, 2022

import numpy as np


class InvalidProbabilityAmplitude(Exception):
    pass


class Qbit:

    # constructor calls validate_amplitudes method
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        self.validate_amplitudes()

    # experiment method runs test 100 times
    def experiment(self):

        # percentage a 0 measured in a trial of 100 tests
        zero_percentage = float((np.random.binomial(100, self.prob_amplitudes()[0], 1)) / 100)

        # percentage a 1 is measured in a trial of 100 tests
        one_percentage = float(1 - zero_percentage)

        return print(f"Percentage of 0's measured: {round(zero_percentage, 2)}\nPercentage of 1's measured:"
                     f" {round(one_percentage, 2)}\n")

    # Calculates probability of 0 or 1 state
    def prob_amplitudes(self):
        prob_0 = self.alpha**2
        prob_1 = self.beta**2

        probability = (prob_0, prob_1)

        return probability

    # Validates zero and ones amplitudes are valid ( == 1)
    # Raises exception if amplitude != 1
    def validate_amplitudes(self):
        num1 = self.prob_amplitudes()[0]
        num2 = self.prob_amplitudes()[1]

        if round(num1 + num2, 3) != 1:
            raise InvalidProbabilityAmplitude

    # string method for printing
    def __str__(self):
        return f'{self.alpha}|0> + {self.beta}|1>'
