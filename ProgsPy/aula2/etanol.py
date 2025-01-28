import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Coordenadas dos átomos
carbon1 = np.array([0, 0, 0])  # Carbono 1
carbon2 = np.array([1.54, 0, 0])  # Carbono 2 (distância C-C de ~1.54 Å)
oxygen = np.array([1.54 + 1.43, 0.96, 0])  # Oxigênio (distância C-O de ~1.43 Å)
hydrogen1 = np.array([-0.54, 0.93, 0])  # Hidrogênio 1 no carbono 1
hydrogen2 = np.array([-0.54, -0.93, 0])  # Hidrogênio 2 no carbono 1
hydrogen3 = np.array([0, 0, 1.02])  # Hidrogênio 3 no carbono 1
hydrogen4 = np.array([1.54, 0.93, 0])  # Hidrogênio 4 no carbono 2
hydrogen5 = np.array([1.54, -0.93, 0])  # Hidrogênio 5 no carbono 2
hydrogen6 = np.array([1.54 + 1.43, 0.96 + 0.96, 0])  # Hidrogênio 6 no oxigênio

# Configuração do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhar os átomos de carbono
ax.scatter(carbon1[0], carbon1[1], carbon1[2], color='black', s=100, label='Carbono (C)')
ax.scatter(carbon2[0], carbon2[1], carbon2[2], color='black', s=100)

# Desenhar o átomo de oxigênio
ax.scatter(oxygen[0], oxygen[1], oxygen[2], color='red', s=100, label='Oxigênio (O)')

# Desenhar os átomos de hidrogênio
ax.scatter(hydrogen1[0], hydrogen1[1], hydrogen1[2], color='blue', s=50, label='Hidrogênio (H)')
ax.scatter(hydrogen2[0], hydrogen2[1], hydrogen2[2], color='blue', s=50)
ax.scatter(hydrogen3[0], hydrogen3[1], hydrogen3[2], color='blue', s=50)
ax.scatter(hydrogen4[0], hydrogen4[1], hydrogen4[2], color='blue', s=50)
ax.scatter(hydrogen5[0], hydrogen5[1], hydrogen5[2], color='blue', s=50)
ax.scatter(hydrogen6[0], hydrogen6[1], hydrogen6[2], color='blue', s=50)

# Desenhar as ligações entre os átomos
# Ligações C-C e C-H
ax.plot([carbon1[0], carbon2[0]], [carbon1[1], carbon2[1]], [carbon1[2], carbon2[2]], color='gray', linewidth=2)
ax.plot([carbon1[0], hydrogen1[0]], [carbon1[1], hydrogen1[1]], [carbon1[2], hydrogen1[2]], color='gray', linewidth=2)
ax.plot([carbon1[0], hydrogen2[0]], [carbon1[1], hydrogen2[1]], [carbon1[2], hydrogen2[2]], color='gray', linewidth=2)
ax.plot([carbon1[0], hydrogen3[0]], [carbon1[1], hydrogen3[1]], [carbon1[2], hydrogen3[2]], color='gray', linewidth=2)
ax.plot([carbon2[0], hydrogen4[0]], [carbon2[1], hydrogen4[1]], [carbon2[2], hydrogen4[2]], color='gray', linewidth=2)
ax.plot([carbon2[0], hydrogen5[0]], [carbon2[1], hydrogen5[1]], [carbon2[2], hydrogen5[2]], color='gray', linewidth=2)

# Ligação C-O e O-H
ax.plot([carbon2[0], oxygen[0]], [carbon2[1], oxygen[1]], [carbon2[2], oxygen[2]], color='gray', linewidth=2)
ax.plot([oxygen[0], hydrogen6[0]], [oxygen[1], hydrogen6[1]], [oxygen[2], hydrogen6[2]], color='gray', linewidth=2)

# Configurações do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Molécula de Etanol (C₂H₆O)')
ax.legend()

# Ajustar os limites dos eixos para melhor visualização
ax.set_xlim([-1, 3])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])

# Mostrar o gráfico
plt.show()