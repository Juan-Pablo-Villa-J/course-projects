import numpy as np
from collections.abc import Callable


def mesh_function(f: Callable[[float], float], t: np.ndarray) -> np.ndarray:
    for j in range(len(t)):
        out[j]=f(t)
    return out
    #raise NotImplementedError


def func(t: float) -> float:
    return np.exp(-t)
    #raise NotImplementedError


def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == "__main__":
    test_mesh_function()
