import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    q = np.asarray(q, dtype=float)
    sorted_x = np.sort(x)
    n = x.size
    r = (q/100)*(n-1)
    l= np.floor(r).astype(int)
    u = np.ceil(r).astype(int)
    w = r - l
    return (1- w)*sorted_x[l]+w*sorted_x[u]