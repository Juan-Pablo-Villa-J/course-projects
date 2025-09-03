import numpy as np


def differentiate(u: np.ndarray, dt: float) -> np.ndarray:
    d[0]=(u[0]+u[1])/2
    for j in range(1,len(u))
        d[j]=(u[j]+u[j+1])/2
    return d
    #raise NotImplementedError

def differentiate_vector(u: np.ndarray, dt: float) -> np.ndarray:
    u_lag=u[:-1]
    u_forward=u[1:]
    d[0]=(u[0]+u[1])/2
    d[1:]=(u_lag+u_forward)/2
    return d
    #raise NotImplementedError

def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()
    