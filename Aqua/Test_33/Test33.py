from datasets import *
from qiskit_aqua.utils import split_dataset_to_data_and_labels, map_label_to_class_name
from qiskit_aqua.input import SVMInput
from qiskit_aqua import run_algorithm, set_aqua_logging

import logging
set_aqua_logging(logging.DEBUG)

n = 2 # dimension of each data point
training_dataset_size = 20
testing_dataset_size = 10

sample_Total, training_input, test_input, class_labels = ad_hoc_data(training_size=training_dataset_size, 
                                                                     test_size=testing_dataset_size, 
                                                                     n=n, gap=0.3, PLOT_DATA=False)

datapoints, class_to_label = split_dataset_to_data_and_labels(test_input)
print(class_to_label)

params = {
    'problem': {'name': 'svm_classification', 'random_seed': 10598},
    'algorithm': {'name': 'QSVM.Variational', 'override_SPSA_params': True},
    'backend': {'name': 'qasm_simulator', 'shots': 1024},
    'optimizer': {'name': 'SPSA', 'max_trials': 200, 'save_steps': 1},
    'variational_form': {'name': 'RYRZ', 'depth': 3},
    'feature_map': {'name': 'SecondOrderExpansion', 'depth': 2}
}

algo_input = SVMInput(training_input, test_input, datapoints[0])

result = run_algorithm(params, algo_input)
print("testing success ratio: ", result['testing_accuracy'])
print("predicted classes:", result['predicted_classes'])
