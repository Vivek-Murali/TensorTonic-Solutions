import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    # Write code here
    indices = {word: index for index, word in enumerate(vocab)}
    counts = np.zeros(len(vocab), dtype=int)

    for token in tokens:
        if token in indices:
            counts[indices[token]] += 1

    return counts