import csv

file_path = 'scop.txt'

# Read the file and process the data
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    # Create a list of tuples (label, seq)
    sequences = [(row['label'], row['seq']) for row in reader]

# Sort by the length of the sequence
sorted_sequences = sorted(sequences, key=lambda x: len(x[1]))

# Print the sorted list of tuples
for label, seq in sorted_sequences:
    print(f"{label}: {seq}")
