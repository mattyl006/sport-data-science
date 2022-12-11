def split_sequences_by_half(sequences):
        first_half_sequences = []
        second_half_sequences = []
        for i, s in enumerate(sequences):
                if 'Half End' in s['type'].values:
                        second_half_sequences = sequences[i+1:]
                        first_half_sequences = sequences[:i+1]
                        break
        return (first_half_sequences, second_half_sequences)