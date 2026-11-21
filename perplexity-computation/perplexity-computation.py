import math
import numpy as np

def perplexity(prob_distributions: list, actual_tokens: list) -> float:
    """
    Returns the sequence perplexity.
    """
    # Write code here
    log_probabilities = []
    for i in range(len(actual_tokens)):
        p_i = prob_distributions[i][actual_tokens[i]]
        log_probabilities.append(np.log(p_i))

    average_log_probability = sum(log_probabilities) / len(log_probabilities)

    return round(np.exp(-average_log_probability),4)
        