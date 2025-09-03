import numpy as np


def differentiate(u: np.ndarray, dt: float) -> np.ndarray:
    N=len(u)                        # Good idea to keep this as a parameter
    d = np.zeros(N)                 # Initialize the output array
    d[0]=(u[1]-u[0])/dt                # Set the first element with forward difference
    d[-1]=(u[-1]-u[-2])/dt            # Set last element with backward difference
    for j in range(1,N-1,1):        # Set counter in the middle
        d[j]=(u[j+1]-u[j-1])/dt/2        # Use mid-points
    return d

def differentiate_vector(u: np.ndarray, dt: float) -> np.ndarray:
    N=len(u)                               # It is nice to have an N
    d = np.zeros(N)                      # Initialize the output array
    d[0]=(u[1]-u[0])/dt                # Set the first element with forward difference
    d[-1]=(u[-1]-u[-2])/dt            # Set last element with backward difference
    d[1:-2]=(u[1:]-u[:-1])/dt/2        #    Compute with mid-points
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
    
