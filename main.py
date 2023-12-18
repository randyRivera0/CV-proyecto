import numpy as np

radio = float(input("Escriba el valor del radio a: "))
intervalos = int(input("Escriba el valor del numero de intervalos: "))

def midpoint_integration(f, a, b, intervals):
    # Generate evenly spaced points between a and b
    x_values = np.linspace(a, b, intervals + 1)

    # Calculate the midpoints of each subinterval
    midpoints = (x_values[:-1] + x_values[1:]) / 2

    # Calculate the function values at each midpoint
    y_values = f(midpoints)

    # Calculate the width of each subinterval
    dx = (b - a) / intervals

    # Apply the midpoint rule for approximation
    integral_approximation = dx * np.sum(y_values)

    return integral_approximation

# Example usage:
# Define your function
def my_function(x):
    return (radio * np.sqrt(5 - np.sin(2 * x))) / 2

# Set integration bounds
a = 0
b = 2 * np.pi

# Set the number of intervals
intervals = intervalos

# Calculate the definite integral using the midpoint rule
result = midpoint_integration(my_function, a, b, intervals)

print(f"La longitud de arco de la traza es con radio {radio} y con {intervalos} intervalos es: {result}")