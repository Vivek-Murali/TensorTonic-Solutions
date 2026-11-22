import numpy as np

def sample_var_std(x: list) -> dict:
    x = np.asarray(x, dtype=float)
    variance = float(np.sum((x - np.mean(x))**2) / (x.size - 1))
    standard_deviation = float(np.sqrt(variance))
    # variance = float(np.var(x, ddof=1))
    # standard_deviation = float(np.std(x, ddof=1))


    return {
        "variance": variance,
        "standard_deviation": standard_deviation
    }
