def plotly_plot(observations, labels):
    # Import necessary libraries
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    # Create 3D scatter plot
    fig1 = go.Figure(data=[go.Scatter3d(x=observations[:, 0], y=observations[:, 1], z=observations[:, 2],
                                        mode='markers',
                                        marker=dict(
        size=3,                 # Increase the size of the markers
        color=labels,                # set color to z-axis value
        colorscale='twilight',   # choose a colorscale
        opacity=0.8
    )
    )])

    # Add title and labels
    fig1.update_layout(
        title='3D Scatter Plot',
        scene=dict(
            xaxis=dict(title='X-axis'),
            yaxis=dict(title='Y-axis'),
            zaxis=dict(title='Z-axis')
        ),
        width=1200,  # Set the width of the figure
        height=800  # Set the height of the figure
    )

    # Create 2D scatter plot of x and y
    fig2 = go.Figure(data=go.Scatter(
        x=observations[:, 0],
        y=observations[:, 1],
        mode='markers',
        marker=dict(
            size=5,
            color=labels,
            colorscale='Viridis',
            opacity=0.5
        ),
    ))

    # Add title and labels for the 2D scatter plot
    fig2.update_layout(
        title='2D Scatter Plot',
        xaxis=dict(title='X-axis', showgrid=True),
        yaxis=dict(title='Y-axis', showgrid=True),
        width=900,
        height=600,
        showlegend=False

    )

    # Create subplots with the 3D scatter plot and the 2D scatter plot

    fig = make_subplots(rows=1, cols=2, specs=[
        [{'type': 'xy'}, {'type': 'scene'}]], subplot_titles=('2D Plot', '3D Plot'))

    fig.add_trace(fig2.data[0], row=1, col=1)
    fig.add_trace(fig1.data[0], row=1, col=2)

    # Update layout for the subplots
    fig.update_layout(height=600, width=1200, showlegend=False)

    # Write the HTML file and show the figure
    fig.show(width=800, height=600)
    fig1.write_html("scatter_plot.html")

# ...
