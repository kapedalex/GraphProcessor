import os
from GraphProcessor import GraphProcessor

def main():
    experiment_folder = 'experiment_example'  # Name of your specific experiment folder
    data_folder = os.path.join(experiment_folder, 'data')
    results_folder = os.path.join(experiment_folder, 'results')

    os.makedirs(results_folder, exist_ok=True)

    input_file = os.path.join(data_folder, 'input.txt')
    output_file = os.path.join(results_folder, 'output.txt')

    # Read input and process it
    NV, NE, edges, rules = GraphProcessor.read_input(input_file)
    processor = GraphProcessor(NV, NE, edges, rules)
    attributes = processor.process_rules()

    # Write the output to the specified file
    processor.write_output(output_file, NV, NE, attributes)

if __name__ == '__main__':
    main()
