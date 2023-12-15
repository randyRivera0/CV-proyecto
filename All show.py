import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

radio = float(input("Escriba el valor del radio a: "))

# File 1: Create data for the existing surface plot
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(x, y)
Z = -0.5 * X -0.5 * Y + 4

# Create a circular cylinder
theta = np.linspace(0, 2 * np.pi, 100)
# r = 0.5 # radius of the cylinder 0.5 default
r = radio  # set radius 
h = 10  # height of the cylinder

X_cylinder = r * np.cos(theta)
Y_cylinder = r * np.sin(theta)

# Repeat the z value for each point on the cylinder to create the height
Z_cylinder = np.linspace(0, h, 100)

# Create a 3D plot for the existing surface
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')

# Plot the existing surface
surf = ax1.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')

# Plot the circular cylinder using the Cylinder class
ax1.plot_surface(X_cylinder, Y_cylinder, Z_cylinder[:, None],
                 color='red', alpha=0.7)

# Set axis labels for the existing surface plot
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Surface Plot with Cylinder')

# File 2: Parametrize the intersection
t = np.linspace(0, 2 * np.pi, 100)
x = np.cos(t)
y = np.sin(t)
z = (8 - np.cos(t) - np.sin(t)) / 2

# Create a 3D plot for the parametrization
ax2 = fig.add_subplot(122, projection='3d')

# Plot the parametrization
ax2.plot(x, y, z, label='Parametrización')

# Set axis labels for the parametrization plot
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Intersection Parametrization')
ax2.legend()

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
