# ket_comp

Qbit has a 0 and 1 state.

Text file: first value is Qbit 0 state, second value is Qbit 1 state
           Remaining values in line are operators to be performed on the initial qbit

Quantum Computation Example:

Main : Reads given text file and implements the required operators in the text file

qbit:  Chcecks the qbit for a valid amplitude (0^2 + 1^2 must = 1)
       Performs binomial distribution 100 times to guess state of the qbit

Single Operator:  Parent class of Hadamard and PauliX operators.
                  Takes a operator matrix and performs dot product on Qbit to get updated state

PauliX operator:  Pauli X Gate operator performed

Haddamard operator:  Haddamard operator performed
