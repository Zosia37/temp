import random
import re

def generate_random_rna(length):
    """Generate a random RNA sequence of the given length."""
    bases = ['A', 'U', 'G', 'C']
    return ''.join(random.choice(bases) for _ in range(length))

def introduce_deletion(sequence):
    """Introduce a deletion at a random position in the sequence."""
    if len(sequence) == 0:
        return sequence
    position = random.randint(0, len(sequence) - 1)
    return sequence[:position] + sequence[position + 1:]

def count_stop_codons(sequence):
    """Count the occurrences of UAG and UGA stop codons."""
    stop_codon_pattern = r'(UAG|UGA)'
    return len(re.findall(stop_codon_pattern, sequence))

# Example usage
length = 50
rna_sequence = generate_random_rna(length)
print(f"Original RNA sequence: {rna_sequence}")

mutated_sequence = introduce_deletion(rna_sequence)
print(f"Mutated RNA sequence: {mutated_sequence}")

stop_codon_count = count_stop_codons(mutated_sequence)
print(f"Number of stop codons (UAG, UGA): {stop_codon_count}")

