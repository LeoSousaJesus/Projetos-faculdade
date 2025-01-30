import plotly.graph_objects as go
import numpy as np

# Parâmetros da dupla hélice
radius = 10  # Raio da hélice
pitch = 30  # Altura de uma volta completa da hélice
num_turns = 3  # Número de voltas da hélice
num_points = 100  # Número de pontos por volta

# Criar as coordenadas da hélice
theta = np.linspace(0, num_turns * 2 * np.pi, num_points * num_turns)  # Ângulo
z = np.linspace(0, pitch * num_turns, num_points * num_turns)  # Altura
x = radius * np.cos(theta)  # Coordenada X
y = radius * np.sin(theta)  # Coordenada Y

# Criar as fitas da dupla hélice
fita1 = go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines',
    line=dict(color='blue', width=5),
    name='Fita 1'
)

fita2 = go.Scatter3d(
    x=-x, y=-y, z=z,
    mode='lines',
    line=dict(color='red', width=5),
    name='Fita 2'
)

# Criar as ligações entre as fitas (pares de bases)
ligacoes = []
for i in range(0, len(x), 10):  # A cada 10 pontos, criar uma ligação
    ligacoes.append(
        go.Scatter3d(
            x=[x[i], -x[i]],
            y=[y[i], -y[i]],
            z=[z[i], z[i]],
            mode='lines',
            line=dict(color='gray', width=2),
            hoverinfo='none',
            showlegend=False
        )
    )

# Criar o layout
layout = go.Layout(
    title='Estrutura do DNA (Dupla Hélice)',
    scene=dict(
        xaxis=dict(title='X (Å)'),
        yaxis=dict(title='Y (Å)'),
        zaxis=dict(title='Z (Å)'),
    ),
    margin=dict(l=0, r=0, b=0, t=30),
    showlegend=True
)

# Criar a figura
fig = go.Figure(data=[fita1, fita2] + ligacoes, layout=layout)

# Mostrar a figura interativa
fig.show()