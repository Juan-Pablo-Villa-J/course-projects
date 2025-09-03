import numpy as np


def differentiate(u: np.ndarray, dt: float) -> np.ndarray:
    d = np.zeros_like(u)  # Initialize the output array
    d[0]=(u[1]-u[0])/dt
    for j in range(1,len(u)-1):
        d[j]=(u[j+1]-u[j-1])/dt
    return d

def differentiate_vector(u: np.ndarray, dt: float) -> np.ndarray:
    d = np.zeros_like(u)  # Initialize the output array
    u_forward=u[:-1]
    u_lag=u[1:]
    d[0]=(u[1]-u[0])/dt
    d[1:]=(u_forward-u_lag)/dt
    return d


def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()
    