import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

"""
Proyecto calculo:
2. Elaboración de un programa ejecutable, en el lenguaje de su elección, que
aproxime la longitud de la traza entre el cilindro x2 + y2 = a2, a > 0, y el
plano x + y + 2z = 8, programando una suma de Riemann de la función sub-
integral que se emplea para el cálculo de longitud de arco. El programa debe
permitir que el usuario ingrese el valor de a en centímetros y la cantidad de
sub-intervalos elegidos para la aproximación.

1. parametrizar el cilindro

x

"""

# Create data for the existing surface plot
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(x, y)
Z = -0.5 * X -0.5 * Y + 4

# Create a circular cylinder
theta = np.linspace(0, 2 * np.pi, 100)
r = 0.5  # radius of the cylinder
h = 10  # height of the cylinder

X_cylinder = r * np.cos(theta)
Y_cylinder = r * np.sin(theta)

# Repeat the z value for each point on the cylinder to create the height
Z_cylinder = np.linspace(0, h, 100)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the existing surface
surf = ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')

# Plot the circular cylinder using the Cylinder class
ax.plot_surface(X_cylinder, Y_cylinder, Z_cylinder[:, None],
                color='red', alpha=0.7)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()