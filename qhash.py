import math
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.quantum_info import Statevector
from qiskit.quantum_info.operators import Pauli

TOTAL_BITS = 16
FRACTION_BITS = 15
# This sets up how many bits are used for fixed-point conversion later.  1 bit for sign, 15 bits for fraction.



# convert a float expectation to fixed-point
def toFixed(x: float) -> int:
    fraction_mult = 1 << FRACTION_BITS
    return int(x * fraction_mult + (0.5 if x >= 0 else -0.5))

# This helper funciton converts a float between -1 and 1 to a 16-bit signed fiexed-point integer. This is 
# used later to encode qunatum measurement results int to a form that can be hashe dor stored.


NUM_QUBITS = 16
NUM_LAYERS = 2

# build the parameterized quantum circuit.
qc = QuantumCircuit(NUM_QUBITS)
params = []


# this defines the quantum circuit with 16 qubits and 2 layers of quantum gates. 
# parms will hodl all symbolic parameters for gate angles
for l in range(NUM_LAYERS):
    # add parameterized RY rotation gates
    for i in range(NUM_QUBITS):
        theta = Parameter(f"theta_ry_{l}_{i}")
        params.append(theta)
        qc.ry(theta, i)
    # add parameterized RX rotation gates
    for i in range(NUM_QUBITS):
        theta = Parameter(f"theta_rz_{l}_{i}")
        params.append(theta)
        qc.rz(theta, i)
    # add CNOT entangling gates
    for i in range(NUM_QUBITS - 1):
        qc.cx(i, i + 1)

# Each layer adds a rotation around Y (RY) and rotation around Z (RZ) for each qubit, parameterized by a variable angle (i.e. not hardcoded).

# After each set of RY and RZ gates, CNOT gates entangle each qubit with its neighbor.

# You’re effectively building a variational (parameterized) quantum circuit.

num_params = len(params)

# Quantum simulation portion of the qhash
# x - 256-bit byte array
# returns the hash value as a 256-bit byte array
def qhash(x: bytes) -> bytes:
    # This function takes a 256-bit input (32 bytes) and returns a quantum-derived hash.
    # create a dictionary mapping each parameter to its value.
    param_values = {}
    for i in range(num_params):
        # extract a nibble (4 bits) from the hash
        nibble = (x[i // 2] >> (4 * (1 - (i % 2)))) & 0x0F
        # scale it to use as a rotation angle parameter
        value = nibble * math.pi / 8
        param_values[params[i]] = value

    # bind the parameters to the circuit.
    bound_qc = qc.assign_parameters(param_values)

    # prepare the state vector from the bound circuit
    sv = Statevector.from_instruction(bound_qc)
    # calculate the qubit expectations on the Z axis
    exps = [sv.expectation_value(Pauli("Z"), [i]).real for i in range(NUM_QUBITS)]
    # convert the expectations to the fixed-point values
    fixed_exps = [toFixed(exp) for exp in exps]

    # pack the fixed-point results into a byte list.
    data = []
    for fixed in fixed_exps:
        for i in range(TOTAL_BITS // 8):
            data.append((fixed >> (8 * i)) & 0xFF)

    return bytes(data)


# #This lacks the full blockchain-specific classical hashign, and restricts the input to a fixed size (256-bits).

# #it is not eligible for a challenge solution in its current form. A proper Qubitcoin implementation would need:

# Post-simulation classical hashing for additional security,

# The ability to handle variable input sizes, and

# A more robust approach to ensuring that the hash result can be used securely in the blockchain’s Proof of Work or Proof of Stake systems.