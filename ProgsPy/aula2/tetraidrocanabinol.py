import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Coordenadas aproximadas dos átomos (simplificado)
# Anel aromático (benzeno)
carbon1 = np.array([0, 0, 0])  # Carbono 1
carbon2 = np.array([1.4, 0, 0])  # Carbono 2
carbon3 = np.array([2.8, 0, 0])  # Carbono 3
carbon4 = np.array([3.5, 1.2, 0])  # Carbono 4
carbon5 = np.array([2.8, 2.4, 0])  # Carbono 5
carbon6 = np.array([1.4, 2.4, 0])  # Carbono 6

# Anel ciclo-hexano
carbon7 = np.array([0, 1.2, 0])  # Carbono 7
carbon8 = np.array([-1.4, 1.2, 0])  # Carbono 8
carbon9 = np.array([-2.1, 0, 0])  # Carbono 9
carbon10 = np.array([-1.4, -1.2, 0])  # Carbono 10
carbon11 = np.array([0, -1.2, 0])  # Carbono 11

# Cadeias laterais e grupo funcional
carbon12 = np.array([-2.1, -2.4, 0])  # Carbono 12
oxygen1 = np.array([-3.5, -2.4, 0])  # Oxigênio 1
carbon13 = np.array([-4.2, -1.2, 0])  # Carbono 13

# Configuração do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhar os átomos de carbono
carbons = [carbon1, carbon2, carbon3, carbon4, carbon5, carbon6, carbon7, carbon8, carbon9, carbon10, carbon11, carbon12, carbon13]
for i, carbon in enumerate(carbons):
    ax.scatter(carbon[0], carbon[1], carbon[2], color='black', s=100, label='Carbono (C)' if i == 0 else "")

# Desenhar o átomo de oxigênio
ax.scatter(oxygen1[0], oxygen1[1], oxygen1[2], color='red', s=100, label='Oxigênio (O)')

# Desenhar as ligações entre os átomos
# Ligações do anel aromático
ax.plot([carbon1[0], carbon2[0]], [carbon1[1], carbon2[1]], [carbon1[2], carbon2[2]], color='gray', linewidth=2)
ax.plot([carbon2[0], carbon3[0]], [carbon2[1], carbon3[1]], [carbon2[2], carbon3[2]], color='gray', linewidth=2)
ax.plot([carbon3[0], carbon4[0]], [carbon3[1], carbon4[1]], [carbon3[2], carbon4[2]], color='gray', linewidth=2)
ax.plot([carbon4[0], carbon5[0]], [carbon4[1], carbon5[1]], [carbon4[2], carbon5[2]], color='gray', linewidth=2)
ax.plot([carbon5[0], carbon6[0]], [carbon5[1], carbon6[1]], [carbon5[2], carbon6[2]], color='gray', linewidth=2)
ax.plot([carbon6[0], carbon1[0]], [carbon6[1], carbon1[1]], [carbon6[2], carbon1[2]], color='gray', linewidth=2)

# Ligações do anel ciclo-hexano
ax.plot([carbon1[0], carbon7[0]], [carbon1[1], carbon7[1]], [carbon1[2], carbon7[2]], color='gray', linewidth=2)
ax.plot([carbon7[0], carbon8[0]], [carbon7[1], carbon8[1]], [carbon7[2], carbon8[2]], color='gray', linewidth=2)
ax.plot([carbon8[0], carbon9[0]], [carbon8[1], carbon9[1]], [carbon8[2], carbon9[2]], color='gray', linewidth=2)
ax.plot([carbon9[0], carbon10[0]], [carbon9[1], carbon10[1]], [carbon9[2], carbon10[2]], color='gray', linewidth=2)
ax.plot([carbon10[0], carbon11[0]], [carbon10[1], carbon11[1]], [carbon10[2], carbon11[2]], color='gray', linewidth=2)
ax.plot([carbon11[0], carbon1[0]], [carbon11[1], carbon1[1]], [carbon11[2], carbon1[2]], color='gray', linewidth=2)

# Ligações das cadeias laterais
ax.plot([carbon9[0], carbon12[0]], [carbon9[1], carbon12[1]], [carbon9[2], carbon12[2]], color='gray', linewidth=2)
ax.plot([carbon12[0], oxygen1[0]], [carbon12[1], oxygen1[1]], [carbon12[2], oxygen1[2]], color='gray', linewidth=2)
ax.plot([oxygen1[0], carbon13[0]], [oxygen1[1], carbon13[1]], [oxygen1[2], carbon13[2]], color='gray', linewidth=2)

# Configurações do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Molécula de THC (C₂₁H₃₀O₂)')
ax.legend()

# Ajustar os limites dos eixos para melhor visualização
ax.set_xlim([-5, 5])
ax.set_ylim([-3, 3])
ax.set_zlim([-1, 1])

# Mostrar o gráfico
plt.show()