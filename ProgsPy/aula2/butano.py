import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Coordenadas dos átomos
carbon1 = np.array([0, 0, 0])  # Carbono 1
carbon2 = np.array([1.54, 0, 0])  # Carbono 2 (distância C-C de ~1.54 Å)
carbon3 = np.array([3.08, 0, 0])  # Carbono 3
carbon4 = np.array([4.62, 0, 0])  # Carbono 4

# Hidrogênios ligados ao carbono 1
hydrogen1 = np.array([-0.54, 0.93, 0])  # Hidrogênio 1
hydrogen2 = np.array([-0.54, -0.93, 0])  # Hidrogênio 2
hydrogen3 = np.array([0, 0, 1.02])  # Hidrogênio 3

# Hidrogênios ligados ao carbono 2
hydrogen4 = np.array([1.54, 0.93, 0])  # Hidrogênio 4
hydrogen5 = np.array([1.54, -0.93, 0])  # Hidrogênio 5

# Hidrogênios ligados ao carbono 3
hydrogen6 = np.array([3.08, 0.93, 0])  # Hidrogênio 6
hydrogen7 = np.array([3.08, -0.93, 0])  # Hidrogênio 7

# Hidrogênios ligados ao carbono 4
hydrogen8 = np.array([4.62, 0.93, 0])  # Hidrogênio 8
hydrogen9 = np.array([4.62, -0.93, 0])  # Hidrogênio 9
hydrogen10 = np.array([4.62, 0, 1.02])  # Hidrogênio 10

# Configuração do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhar os átomos de carbono
ax.scatter(carbon1[0], carbon1[1], carbon1[2], color='black', s=100, label='Carbono (C)')
ax.scatter(carbon2[0], carbon2[1], carbon2[2], color='black', s=100)
ax.scatter(carbon3[0], carbon3[1], carbon3[2], color='black', s=100)
ax.scatter(carbon4[0], carbon4[1], carbon4[2], color='black', s=100)

# Desenhar os átomos de hidrogênio
ax.scatter(hydrogen1[0], hydrogen1[1], hydrogen1[2], color='blue', s=50, label='Hidrogênio (H)')
ax.scatter(hydrogen2[0], hydrogen2[1], hydrogen2[2], color='blue', s=50)
ax.scatter(hydrogen3[0], hydrogen3[1], hydrogen3[2], color='blue', s=50)
ax.scatter(hydrogen4[0], hydrogen4[1], hydrogen4[2], color='blue', s=50)
ax.scatter(hydrogen5[0], hydrogen5[1], hydrogen5[2], color='blue', s=50)
ax.scatter(hydrogen6[0], hydrogen6[1], hydrogen6[2], color='blue', s=50)
ax.scatter(hydrogen7[0], hydrogen7[1], hydrogen7[2], color='blue', s=50)
ax.scatter(hydrogen8[0], hydrogen8[1], hydrogen8[2], color='blue', s=50)
ax.scatter(hydrogen9[0], hydrogen9[1], hydrogen9[2], color='blue', s=50)
ax.scatter(hydrogen10[0], hydrogen10[1], hydrogen10[2], color='blue', s=50)

# Desenhar as ligações entre os átomos
# Ligações C-C
ax.plot([carbon1[0], carbon2[0]], [carbon1[1], carbon2[1]], [carbon1[2], carbon2[2]], color='gray', linewidth=2)
ax.plot([carbon2[0], carbon3[0]], [carbon2[1], carbon3[1]], [carbon2[2], carbon3[2]], color='gray', linewidth=2)
ax.plot([carbon3[0], carbon4[0]], [carbon3[1], carbon4[1]], [carbon3[2], carbon4[2]], color='gray', linewidth=2)

# Ligações C-H
ax.plot([carbon1[0], hydrogen1[0]], [carbon1[1], hydrogen1[1]], [carbon1[2], hydrogen1[2]], color='gray', linewidth=2)
ax.plot([carbon1[0], hydrogen2[0]], [carbon1[1], hydrogen2[1]], [carbon1[2], hydrogen2[2]], color='gray', linewidth=2)
ax.plot([carbon1[0], hydrogen3[0]], [carbon1[1], hydrogen3[1]], [carbon1[2], hydrogen3[2]], color='gray', linewidth=2)
ax.plot([carbon2[0], hydrogen4[0]], [carbon2[1], hydrogen4[1]], [carbon2[2], hydrogen4[2]], color='gray', linewidth=2)
ax.plot([carbon2[0], hydrogen5[0]], [carbon2[1], hydrogen5[1]], [carbon2[2], hydrogen5[2]], color='gray', linewidth=2)
ax.plot([carbon3[0], hydrogen6[0]], [carbon3[1], hydrogen6[1]], [carbon3[2], hydrogen6[2]], color='gray', linewidth=2)
ax.plot([carbon3[0], hydrogen7[0]], [carbon3[1], hydrogen7[1]], [carbon3[2], hydrogen7[2]], color='gray', linewidth=2)
ax.plot([carbon4[0], hydrogen8[0]], [carbon4[1], hydrogen8[1]], [carbon4[2], hydrogen8[2]], color='gray', linewidth=2)
ax.plot([carbon4[0], hydrogen9[0]], [carbon4[1], hydrogen9[1]], [carbon4[2], hydrogen9[2]], color='gray', linewidth=2)
ax.plot([carbon4[0], hydrogen10[0]], [carbon4[1], hydrogen10[1]], [carbon4[2], hydrogen10[2]], color='gray', linewidth=2)

# Configurações do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Molécula de Butano (C₄H₁₀)')
ax.legend()

# Ajustar os limites dos eixos para melhor visualização
ax.set_xlim([-1, 6])
ax.set_ylim([-2, 2])
ax.set_zlim([-1, 2])

# Mostrar o gráfico
plt.show()