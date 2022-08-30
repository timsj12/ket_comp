

from hadamard import Hadamard
from paulix import PauliX
from qbit import Qbit

from qbit import InvalidProbabilityAmplitude
from qoperators import InvalidOperator

if __name__ == "__main__":

    # open qubits.txt file interpreting in utf-16 format
    f = open("qubits.txt", "r", encoding='utf-16')

    # read each line in the file
    for line in f.readlines():
        qubit_data = line.strip().split(" ")

        # Assign alpha and beta values from first two values in line
        # create a qubit object and check for proper amplitude
        try:
            alpha = float(qubit_data[0])
            beta = float(qubit_data[1])
            qbit = Qbit(alpha, beta)
        except InvalidProbabilityAmplitude:
            print('Invalid probability amplitude(s).')
            break

        # print initial state of qbit
        print(f'Initial State: {str(qbit)}')

        # Perform operator called out in the line
        try:
            for i in range(2, len(qubit_data)):

                # create hadamard and paulix objects
                # Raise invalid operator exception if H or X operator not requested
                if qubit_data[i] == 'H':
                    hadamard = Hadamard()
                    qbit = hadamard.operate(qbit)
                elif qubit_data[i] == 'X':
                    paulix = PauliX()
                    qbit = paulix.operate(qbit)
                else:
                    raise InvalidOperator

            # print final state and run experiment
            print(f'Final State: {str(qbit)}')
            qbit.experiment()

        except InvalidOperator:
            print('Invalid Operator.\n')

    # close file
    f.close()
