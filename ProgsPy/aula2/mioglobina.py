from Bio.PDB import PDBParser, MMCIFParser
from Bio.PDB.PDBIO import PDBIO
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Baixar a estrutura da mioglobina (1MBN) do PDB
from Bio.PDB import PDBList
pdbl = PDBList()
pdbl.retrieve_pdb_file('1MBN', pdir='.', file_format='pdb')

# Carregar a estrutura
parser = PDBParser()
structure = parser.get_structure('1MBN', 'pdb1mbn.ent')

# Extrair coordenadas dos átomos
atoms = []
for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                atoms.append(atom.coord)

# Converter as coordenadas em um array numpy
atoms = np.array(atoms)

# Configuração do gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotar os átomos
ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], c='blue', s=10, alpha=0.5)

# Configurações do gráfico
ax.set_xlabel('X (Å)')
ax.set_ylabel('Y (Å)')
ax.set_zlabel('Z (Å)')
ax.set_title('Estrutura da Mioglobina (1MBN)')

# Mostrar o gráfico
plt.show()