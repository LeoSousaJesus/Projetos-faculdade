import plotly.graph_objects as go
import numpy as np

# Função para criar uma hélice de RNA
def create_rna_helix(num_points=20, radius=5, pitch=10):
    theta = np.linspace(0, 2 * np.pi, num_points)  # Ângulo
    z = np.linspace(0, pitch, num_points)  # Altura
    x = radius * np.cos(theta)  # Coordenada X
    y = radius * np.sin(theta)  # Coordenada Y
    return x, y, z

# Função para criar uma alça de RNA
def create_rna_loop(num_points=10, radius=5, height=5):
    theta = np.linspace(0, np.pi, num_points)  # Ângulo
    x = radius * np.cos(theta)  # Coordenada X
    y = np.zeros(num_points)  # Coordenada Y (fixa)
    z = height * np.sin(theta)  # Coordenada Z
    return x, y, z

# Criar a hélice de RNA
x_helix, y_helix, z_helix = create_rna_helix()

# Criar a alça de RNA
x_loop, y_loop, z_loop = create_rna_loop()

# Combinar as coordenadas da hélice e da alça
x = np.concatenate([x_helix, x_loop])
y = np.concatenate([y_helix, y_loop])
z = np.concatenate([z_helix, z_loop + z_helix[-1]])  # Ajustar a altura da alça

# Criar a fita de RNA
rna_trace = go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines+markers',
    line=dict(color='green', width=10),
    marker=dict(size=5, color='black'),
    name='RNA'
)

# Criar as ligações (pares de bases na hélice)
ligacoes = []
for i in range(len(x_helix) // 2):
    ligacoes.append(
        go.Scatter3d(
            x=[x_helix[i], x_helix[-(i + 1)]],
            y=[y_helix[i], y_helix[-(i + 1)]],
            z=[z_helix[i], z_helix[-(i + 1)]],
            mode='lines',
            line=dict(color='gray', width=2),
            hoverinfo='none',
            showlegend=False
        )
    )

# Criar o layout
layout = go.Layout(
    title='Estrutura do RNA',
    scene=dict(
        xaxis=dict(title='X (Å)'),
        yaxis=dict(title='Y (Å)'),
        zaxis=dict(title='Z (Å)'),
    ),
    margin=dict(l=0, r=0, b=0, t=30),
    showlegend=True
)

# Criar a figura
fig = go.Figure(data=[rna_trace] + ligacoes, layout=layout)

# Mostrar a figura interativa
fig.show()