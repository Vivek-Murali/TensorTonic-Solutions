import numpy as np

def rnn_step_forward(x_t: list, h_prev: list, Wx: list, Wh: list, b: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (H,).
    """
    # Write code here
    return np.tanh((np.array(x_t)@np.array(Wx)) + (np.array(h_prev)@np.array(Wh)) + np.array(b))