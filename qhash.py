import math
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.quantum_info import Statevector
from qiskit.quantum_info.operators import Pauli

TOTAL_BITS = 16
FRACTION_BITS = 15

# convert a float expectation to fixed-point
def toFixed(x: float) -> int:
    fraction_mult = 1 << FRACTION_BITS
    return int(x * fraction_mult + (0.5 if x >= 0 else -0.5))


NUM_QUBITS = 16
NUM_LAYERS = 2

# build the parameterized quantum circuit.
qc = QuantumCircuit(NUM_QUBITS)
params = []
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
num_params = len(params)

# Quantum simulation portion of the qhash
# x - 256-bit byte array
# returns the hash value as a 256-bit byte array
def qhash(x: bytes) -> bytes:
    # create a dictionary mapping each parameter to its value.
    param_values = {}
    for i in range(num_params):
        # extract a nibble (4 bits) from the hash
        nibble = (in_hash[i // 2] >> (4 * (1 - (i % 2)))) & 0x0F
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
