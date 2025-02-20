import plotly.graph_objects as go

testers = ["Angel", "Tester 2"]
defectos_descubiertos = [0, 1]
total_defectos = 1
porcentaje_defectos = [(x / total_defectos) * 100 for x in defectos_descubiertos]

fig = go.Figure()

fig.add_trace(go.Bar(
    x=testers,
    y=porcentaje_defectos,
    name="Defectos Descubiertos",
    marker=dict(color="orange"),
))

fig.update_layout(
    title="Porcentaje de Defectos Descubiertos por Tester",
    xaxis_title="Tester",
    yaxis_title="Porcentaje de Defectos (%)",
    showlegend=True
)

fig.show()
fig.write_html("testers.html")
