import plotly.graph_objects as go

total_pruebas = 100
pruebas_pasadas = 80
pruebas_fallidas = 20

porcentaje_pasadas = (pruebas_pasadas / total_pruebas) * 100
porcentaje_fallidas = (pruebas_fallidas / total_pruebas) * 100

fig = go.Figure()

fig.add_trace(go.Bar(
    x=["Pruebas Pasadas", "Pruebas Fallidas"],
    y=[pruebas_pasadas, pruebas_fallidas],
    name="Resultados",
    marker=dict(color=["green", "red"]),
    hovertemplate=[
        f"{pruebas_pasadas} de {total_pruebas} pruebas pasadas - {porcentaje_pasadas:.2f}%<extra></extra>",
        f"{pruebas_fallidas} de {total_pruebas} pruebas fallidas - {porcentaje_fallidas:.2f}%<extra></extra>"
    ]
))

fig.update_layout(
    title="Resultados de Pruebas: Pasadas vs Fallidas",
    xaxis_title="Estado de las Pruebas",
    yaxis_title="Número de Pruebas",
    showlegend=False,
    xaxis=dict(tickvals=[0, 1], ticktext=["Pruebas Pasadas", "Pruebas Fallidas"]),
)

fig.show()
fig.write_html("godvsbad.html")
