import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parametrización
t = np.linspace(0, 2 * np.pi, 100)
x = np.cos(t)
y = np.sin(t)
z = (8 - np.cos(t) - np.sin(t)) / 2

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la parametrización
ax.plot(x, y, z, label='Parametrización')

# Configuraciones adicionales
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Intersección entre x^2 + y^2 = 1 y x + y + 2z = 8')
ax.legend()

# Mostrar el gráfico
plt.show()
