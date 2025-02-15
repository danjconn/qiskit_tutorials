# Taken from https://quantumexperience.ng.bluemix.net/qx/tutorial?sectionId=full-user-guide&page=001-The_IBM_Q_Experience~2F003-The_Quantum_Composer

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Define the Quantum and Classical Registers

q = QuantumRegister(2)
c = ClassicalRegister(2)

# Build the circuit
my_first_score = QuantumCircuit(q, c)

# Pauli operations
my_first_score.x(q[0])
my_first_score.y(q[1])
my_first_score.z(q[0])
my_first_score.barrier(q)

# Clifford operations
my_first_score.h(q)
my_first_score.s(q[0])
my_first_score.s(q[1]).inverse()
my_first_score.cx(q[0], q[1])
my_first_score.barrier(q)

# Non-Clifford operations
my_first_score.t(q[0])
my_first_score.t(q[1]).inverse()
my_first_score.barrier(q)

# measurement operations
my_first_score.measure(q,c)

# Execute the circuit
job = execute(my_first_score, backend=Aer.get_backend('qasm_simulator'), shots=1024)
result = job.result()

print(result.get_counts(my_first_score))