import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Coordenadas dos átomos
oxygen = np.array([0, 0, 0])  # Oxigênio no centro
hydrogen1 = np.array([0.95, 0, 0])  # Hidrogênio 1
hydrogen2 = np.array([-0.37, 0.93, 0])  # Hidrogênio 2 (ângulo de ~104,5°)

# Configuração do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhar o átomo de oxigênio
ax.scatter(oxygen[0], oxygen[1], oxygen[2], color='red', s=100, label='Oxigênio (O)')

# Desenhar os átomos de hidrogênio
ax.scatter(hydrogen1[0], hydrogen1[1], hydrogen1[2], color='blue', s=50, label='Hidrogênio (H)')
ax.scatter(hydrogen2[0], hydrogen2[1], hydrogen2[2], color='blue', s=50)

# Desenhar as ligações entre oxigênio e hidrogênio
ax.plot([oxygen[0], hydrogen1[0]], [oxygen[1], hydrogen1[1]], [oxygen[2], hydrogen1[2]], color='gray', linewidth=2)
ax.plot([oxygen[0], hydrogen2[0]], [oxygen[1], hydrogen2[1]], [oxygen[2], hydrogen2[2]], color='gray', linewidth=2)

# Configurações do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Molécula de Água (H₂O)')
ax.legend()

# Ajustar os limites dos eixos para melhor visualização
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Mostrar o gráfico
plt.show()