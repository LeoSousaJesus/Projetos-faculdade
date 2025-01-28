import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Coordenadas dos átomos
carbon = np.array([0, 0, 0])  # Carbono no centro
hydrogens = np.array([
    [1, 1, 1],   # Hidrogênio 1
    [-1, -1, 1], # Hidrogênio 2
    [-1, 1, -1], # Hidrogênio 3
    [1, -1, -1]  # Hidrogênio 4
])

# Configuração do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhar o carbono
ax.scatter(carbon[0], carbon[1], carbon[2], color='black', s=100, label='Carbono (C)')

# Desenhar os hidrogênios
for i, hydrogen in enumerate(hydrogens):
    ax.scatter(hydrogen[0], hydrogen[1], hydrogen[2], color='blue', s=50, label=f'Hidrogênio (H{i+1})')
    # Desenhar as ligações entre carbono e hidrogênio
    ax.plot([carbon[0], hydrogen[0]], [carbon[1], hydrogen[1]], [carbon[2], hydrogen[2]], color='gray')

# Configurações do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Molécula de Metano (CH₄)')
ax.legend()

# Mostrar o gráfico
plt.show()