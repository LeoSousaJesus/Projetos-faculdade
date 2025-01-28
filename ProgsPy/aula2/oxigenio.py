import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Coordenadas dos átomos
oxygen1 = np.array([0, 0, 0])  # Oxigênio 1
oxygen2 = np.array([1.2, 0, 0])  # Oxigênio 2 (distância de ~1.2 Å, comum para ligação O=O)

# Configuração do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhar os átomos de oxigênio
ax.scatter(oxygen1[0], oxygen1[1], oxygen1[2], color='red', s=100, label='Oxigênio (O)')
ax.scatter(oxygen2[0], oxygen2[1], oxygen2[2], color='red', s=100)

# Desenhar a ligação dupla entre os oxigênios
ax.plot([oxygen1[0], oxygen2[0]], [oxygen1[1], oxygen2[1]], [oxygen1[2], oxygen2[2]], color='black', linewidth=2)
ax.plot([oxygen1[0], oxygen2[0]], [oxygen1[1], oxygen2[1]], [oxygen1[2] + 0.1, oxygen2[2] + 0.1], color='black', linewidth=2)

# Configurações do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Molécula de Oxigênio (O₂)')
ax.legend()

# Ajustar os limites dos eixos para melhor visualização
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Mostrar o gráfico
plt.show()