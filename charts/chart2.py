import plotly.graph_objects as go
import plotly.subplots as sp

# Datos
features = ["Nave del jugador - Angel", "Tryout - NN"]
defectos = [0, 2]
actividades_pass = [10, 8]

defectos_features = ["Movimiento de las naves alienigenas", "Movimiento del jugador", "Disparos del jugador", "Disparos del enemigo", "Finalizacion del juego", "Colision y proteccion", "Gestion de vidas y puntuacion", "Persistencia de Datos", "Sincronización del sonido", "resoluciones de pantalla"]
defectos_cantidad = [2, 3, 5, 1, 4, 2, 0,0,0,0]  

fig = sp.make_subplots(
    rows=2, cols=1,
    subplot_titles=(
        "Distribución de Defectos y Actividades por Feature",
        "Defectos por charter"
    ),
    specs=[[{"type": "bar"}], [{"type": "scatter"}]]
)

fig.add_trace(go.Bar(
    x=features,
    y=defectos,
    name="Actividades Fallidas",
    marker=dict(color="red"),
), row=1, col=1)

fig.add_trace(go.Bar(
    x=features,
    y=actividades_pass,
    name="Actividades Pass",
    marker=dict(color="green"),
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=defectos_features,
    y=defectos_cantidad,
    mode="markers+lines",
    marker=dict(size=10, color="red"),
    name="Defectos por Feature"
), row=2, col=1)

fig.update_layout(
    title="Análisis de Actividades y Defectos por Feature",
    height=700,
    barmode="stack",
    xaxis_title="Feature",
    yaxis_title="Número de Elementos",
    showlegend=True
)

fig.show()
fig.write_html("chart2.html")
