import plotly.graph_objects as go

num_defectos = 0
num_pruebas = 10
efectividad = (num_defectos / num_pruebas) * 100 

labels = ["Defectos encontrados", "Pruebas exitosas"]
values = [num_defectos, num_pruebas]

fig = go.Figure()

fig.add_trace(go.Pie(
    labels=labels, 
    values=values, 
    marker=dict(colors=["red", "green"]),
    textinfo="label+percent",
    insidetextorientation="radial"
))

fig.update_layout(
    title="Efectividad de las Pruebas",
    annotations=[
        dict(
            text=f"Efectividad: ({num_defectos} / {num_pruebas}) * 100 = {efectividad:.2f}%",
            x=0.5, y=-0.2,
            font=dict(size=14),
            showarrow=False
        )
    ]
)

fig.show()
fig.write_html("chart1.html")
