import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# File 1: Create data for the existing surface plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Get user input for the radius
radius = float(input("Escriba el valor del radio a: "))

# Parametric equation of the plane
Z_plane = -0.5 * X - 0.5 * Y + 4

# Create a circular cylinder
theta = np.linspace(0, 2 * np.pi, 100)
h = 10  # Set a reasonable height

X_cylinder = radius * np.cos(theta)
Y_cylinder = radius * np.sin(theta)

# Repeat the z value for each point on the cylinder to create the height
Z_cylinder = np.linspace(0, h, 100)

# Create a 3D plot for the existing surface
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection='3d')

# Plot the existing surface
surf = ax1.plot_surface(X, Y, Z_plane, alpha=0.7, cmap='viridis')

# Plot the circular cylinder using the Cylinder class
ax1.plot_surface(X_cylinder, Y_cylinder, Z_cylinder[:, None],
                 color='red', alpha=0.7)

# Set axis labels and adjust limits for the existing surface plot
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Surface Plot with Larger Plane')

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

# Adjust limits and aspect ratio for the parametrization plot
ax2.set_xlim([-2, 2])
ax2.set_ylim([-2, 2])
ax2.set_zlim([0, 8])
ax2.set_box_aspect([1, 1, 0.8])  # Adjust the aspect ratio

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
