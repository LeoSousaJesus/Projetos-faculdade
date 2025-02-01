import plotly.graph_objects as go
import numpy as np

# Coordenadas aproximadas dos átomos da biotina (em Ångstrons)
# Fonte: Adaptado de dados moleculares
atoms = {
    "C1": [0.0, 0.0, 0.0],  # Carbono 1 (anel de ureia)
    "C2": [1.4, 0.0, 0.0],  # Carbono 2 (anel de ureia)
    "N1": [0.7, 1.2, 0.0],  # Nitrogênio 1 (anel de ureia)
    "N2": [0.7, -1.2, 0.0], # Nitrogênio 2 (anel de ureia)
    "O1": [2.1, 0.0, 0.0],  # Oxigênio 1 (carbonila)
    "S1": [-1.4, 0.0, 0.0], # Enxofre (anel de tiofeno)
    "C3": [-2.8, 0.0, 0.0], # Carbono 3 (anel de tiofeno)
    "C4": [-3.5, 1.2, 0.0], # Carbono 4 (anel de tiofeno)
    "C5": [-2.8, 2.4, 0.0], # Carbono 5 (anel de tiofeno)
    "C6": [-1.4, 2.4, 0.0], # Carbono 6 (anel de tiofeno)
    "C7": [2.8, 0.0, 0.0],  # Carbono 7 (cadeia lateral)
    "C8": [3.5, -1.2, 0.0], # Carbono 8 (cadeia lateral)
    "C9": [4.9, -1.2, 0.0], # Carbono 9 (cadeia lateral)
    "C10": [5.6, 0.0, 0.0], # Carbono 10 (cadeia lateral)
    "O2": [5.6, 1.2, 0.0],  # Oxigênio 2 (hidroxila)
}

# Ligações entre os átomos (pares de átomos ligados)
bonds = [
    ("C1", "C2"), ("C1", "N1"), ("C1", "N2"), ("C2", "O1"),
    ("C1", "S1"), ("S1", "C3"), ("C3", "C4"), ("C4", "C5"),
    ("C5", "C6"), ("C6", "S1"), ("C2", "C7"), ("C7", "C8"),
    ("C8", "C9"), ("C9", "C10"), ("C10", "O2")
]

# Criar o gráfico 3D
fig = go.Figure()

# Adicionar os átomos ao gráfico
for atom, (x, y, z) in atoms.items():
    color = 'black'  # Carbono
    if atom.startswith('N'):
        color = 'blue'  # Nitrogênio
    elif atom.startswith('O'):
        color = 'red'  # Oxigênio
    elif atom.startswith('S'):
        color = 'yellow'  # Enxofre
    fig.add_trace(
        go.Scatter3d(
            x=[x], y=[y], z=[z],
            mode='markers',
            marker=dict(size=10, color=color),
            name=atom,
            text=atom,
            hoverinfo='text'
        )
    )

# Adicionar as ligações ao gráfico
for bond in bonds:
    atom1, atom2 = bond
    x1, y1, z1 = atoms[atom1]
    x2, y2, z2 = atoms[atom2]
    fig.add_trace(
        go.Scatter3d(
            x=[x1, x2], y=[y1, y2], z=[z1, z2],
            mode='lines',
            line=dict(color='gray', width=5),
            hoverinfo='none',
            showlegend=False
        )
    )

# Configurações do gráfico
fig.update_layout(
    title='Molécula de Biotina (Vitamina B7)',
    scene=dict(
        xaxis=dict(title='X (Å)'),
        yaxis=dict(title='Y (Å)'),
        zaxis=dict(title='Z (Å)'),
    ),
    margin=dict(l=0, r=0, b=0, t=30),
    showlegend=False
)

# Mostrar o gráfico interativo
fig.show()