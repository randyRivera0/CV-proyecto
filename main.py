from scipy.integrate import quad
import numpy as np

radio = float(input("Escriba el valor del radio a: "))

def trapezoidal_integration(f, a, b, intervals):
    # Generate evenly spaced points between a and b
    x_values = np.linspace(a, b, intervals + 1)
    
    # Calculate the function values at each point
    y_values = f(x_values)
    
    # Calculate the width of each subinterval
    dx = (b - a) / intervals
    
    # Apply the trapezoidal rule for approximation
    integral_approximation = dx * (0.5 * y_values[0] + np.sum(y_values[1:-1]) + 0.5 * y_values[-1])
    
    return integral_approximation

# Example usage:
# Define your function
def my_function(x):
    return (radio * np.sqrt(5 - np.sin(2*x)))/2

# Set integration bounds
a = 0
b = 2 * np.pi

# Set the number of intervals
intervals = 1000000

# Calculate the definite integral using the trapezoidal rule
result = trapezoidal_integration(my_function, a, b, intervals)
print(f"The definite integral of x^2 from {a} to {b} using {intervals} intervals is approximately: {result}")
