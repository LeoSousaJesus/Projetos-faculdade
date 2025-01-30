import plotly.graph_objects as go
import numpy as np

# Função para criar uma molécula de etileno (C₂H₄)
def create_ethylene(offset_x=0):
    # Coordenadas dos átomos
    carbon1 = np.array([0 + offset_x, 0, 0])  # Carbono 1
    carbon2 = np.array([1.34 + offset_x, 0, 0])  # Carbono 2 (distância C=C de ~1.34 Å)
    hydrogen1 = np.array([-0.97 + offset_x, 0.93, 0])  # Hidrogênio 1
    hydrogen2 = np.array([-0.97 + offset_x, -0.93, 0])  # Hidrogênio 2
    hydrogen3 = np.array([2.31 + offset_x, 0.93, 0])  # Hidrogênio 3
    hydrogen4 = np.array([2.31 + offset_x, -0.93, 0])  # Hidrogênio 4

    # Lista de átomos e ligações
    atoms = [carbon1, carbon2, hydrogen1, hydrogen2, hydrogen3, hydrogen4]
    bonds = [
        (carbon1, carbon2),  # Ligação C=C
        (carbon1, hydrogen1),  # Ligação C-H
        (carbon1, hydrogen2),  # Ligação C-H
        (carbon2, hydrogen3),  # Ligação C-H
        (carbon2, hydrogen4),  # Ligação C-H
    ]

    return atoms, bonds

# Função para criar uma cadeia de moléculas de etileno
def create_ethylene_chain(num_molecules=3, spacing=3):
    all_atoms = []
    all_bonds = []

    for i in range(num_molecules):
        offset_x = i * spacing
        atoms, bonds = create_ethylene(offset_x)
        all_atoms.extend(atoms)
        all_bonds.extend(bonds)

    return all_atoms, all_bonds

# Criar a cadeia de etileno
atoms, bonds = create_ethylene_chain(num_molecules=5, spacing=3)

# Preparar dados para o plotly
atom_trace = go.Scatter3d(
    x=[atom[0] for atom in atoms],
    y=[atom[1] for atom in atoms],
    z=[atom[2] for atom in atoms],
    mode='markers',
    marker=dict(
        size=10,
        color=['black'] * 2 * 5 + ['blue'] * 4 * 5,  # Carbono (preto) e Hidrogênio (azul)
        opacity=0.9
    ),
    text=['C'] * 2 * 5 + ['H'] * 4 * 5,
    name='Átomos'
)

bond_trace = []
for bond in bonds:
    bond_trace.append(
        go.Scatter3d(
            x=[bond[0][0], bond[1][0]],
            y=[bond[0][1], bond[1][1]],
            z=[bond[0][2], bond[1][2]],
            mode='lines',
            line=dict(color='gray', width=5),
            hoverinfo='none',
            showlegend=False
        )
    )

# Criar o layout
layout = go.Layout(
    title='Cadeia de Etileno (C₂H₄)',
    scene=dict(
        xaxis=dict(title='X (Å)'),
        yaxis=dict(title='Y (Å)'),
        zaxis=dict(title='Z (Å)'),
    ),
    margin=dict(l=0, r=0, b=0, t=30),
    showlegend=True
)

# Criar a figura
fig = go.Figure(data=[atom_trace] + bond_trace, layout=layout)

# Mostrar a figura interativa
fig.show()