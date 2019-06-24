# Taken from https://quantumexperience.ng.bluemix.net/proxy/tutorial/full-user-guide/001-The_IBM_Q_Experience/004-Running_your_Quantum_Scores.html

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Define Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build quantum circuit
single_q_measurement = QuantumCircuit(q,c)
single_q_measurement.measure(q,c)

# Execute quantum circuit
job = execute(single_q_measurement, backend = Aer.get_backend('qasm_simulator'), shots=1024)
result = job.result()

# Print result
print(result.get_counts(single_q_measurement))