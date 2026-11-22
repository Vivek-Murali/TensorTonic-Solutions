import numpy as np

def sample_var_std(x: list) -> dict:
    x = np.asarray(x, dtype=float)
    variance = np.sum((x - np.mean(x))**2) / (x.size - 1)
    standard_deviation = np.sqrt(variance)

    return {
        "variance": float(variance),
        "standard_deviation": float(standard_deviation)
    }
