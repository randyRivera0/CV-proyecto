import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def parametrize_cylinder(R, height_range, angle_range):
    t_values = np.linspace(height_range[0], height_range[1], 100)
    theta_values = np.linspace(angle_range[0], angle_range[1], 100)
    
    t, theta = np.meshgrid(t_values, theta_values)

    x = R * np.cos(theta)
    y = R * np.sin(theta)
    z = t
    
    return x, y, z

# Set parameters
radius = 1.0
height_range = (0, 3)
angle_range = (0, 2 * np.pi)

# Parametrize the cylinder
x, y, z = parametrize_cylinder(radius, height_range, angle_range)

# Plot the parametrization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, alpha=0.7)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Parametrization of a Cylinder')

plt.show()
