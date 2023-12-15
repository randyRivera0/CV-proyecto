import numpy as np
from scipy.integrate import quad

def f(t):
    return np.sqrt(5 - np.sin(2*t))

# Set the integration bounds
a = 0
b = 2 * np.pi

# Perform the integration using the quad function
result, _ = quad(f, a, b)

print(f"The definite integral is approximately: {result}")
