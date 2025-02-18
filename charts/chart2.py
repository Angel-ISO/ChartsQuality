import plotly.graph_objects as go

features = ["Nave del jugador- Angel", "tryout- nn"]
defectos = [0, 2]
actividades_pass = [10, 8]  

fig = go.Figure()

fig.add_trace(go.Bar(
    x=features,
    y=defectos,
    name="Defectos",
    marker=dict(color="red"),
))

fig.add_trace(go.Bar(
    x=features,
    y=actividades_pass,
    name="Actividades Pass",
    marker=dict(color="green"),
))

fig.update_layout(
    barmode="stack",
    title="Distribución de Defectos por Feature y Actividades",
    xaxis_title="Feature",
    yaxis_title="Número de Elementos",
    showlegend=True
)

fig.show()
