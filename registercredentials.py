import config
from qiskit import IBMQ
print("Registering credentials stored in config.py. Overwriting any existing ones.")
IBMQ.save_account(config.IBM_Q_API_TOKEN, 'https://quantumexperience.ng.bluemix.net/api', True)
print("Completed registration")