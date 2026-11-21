import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    positions = np.arange(seq_len, dtype=np.float64).reshape(-1, 1)

    num_sin = (d_model + 1) // 2
    num_cos = d_model // 2

    sin_indices = np.arange(num_sin, dtype=np.float64).reshape(1, -1)
    cos_indices = np.arange(num_cos, dtype=np.float64).reshape(1, -1)

    sin_angles = positions / np.power(base, (2 * sin_indices) / d_model)
    cos_angles = positions / np.power(base, (2 * cos_indices) / d_model)

    pe = np.zeros((seq_len, d_model), dtype=np.float64)

    pe[:, 0::2] = np.sin(sin_angles)
    pe[:, 1::2] = np.cos(cos_angles)

    return pe