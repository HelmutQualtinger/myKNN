

import random

import numpy as np

import bokeh
from bokeh.plotting import figure, show
from bokeh.models import LinearColorMapper, CategoricalColorMapper, ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Reds, Blues, Category20
from bokeh.layouts import gridplot


def plot_observations(observations, labels):
    # Extract x and y coordinates from the observations
    x = observations[:, 0]
    y = observations[:, 1]
    z = observations[:, 2]
    # Convert labels to an array of uint32
    labels = np.array(labels, dtype=np.uint32)

    data = {
        'x': x,
        'y': y,
        'z': z,
        'c': labels
    }
    source = ColumnDataSource(data=dict(x=x, y=y, z=z,))

    # Create a colormapper

    color_mapper = LinearColorMapper(
        palette=['red', 'blue', 'green', 'violet'], low=min(labels), high=max(labels))
    # Create a scatter plot
    p1 = figure(title="Observations", x_axis_label="X", y_axis_label="Y")

    p1.scatter(x='x', y='y', fill_color={'field': 'c', 'transform': color_mapper},
               legend_label="Observations", source=source, size=10, fill_alpha=0.9)

    p2 = figure(title="Observations", x_axis_label="Z", y_axis_label="Y")
    p2.scatter(x='z', y='y', fill_color={'field': 'c', 'transform': color_mapper},
               legend_label="Observations", source=source, size=10, fill_alpha=0.9)

    # p3 = figure(title="Observations", x_axis_label="X",
    #             y_axis_label="Y")
    # p3.scatter(x='z', y='y', z='z', fill_color={'field': 'c', 'transform': color_mapper},
    #            legend_label="Observations", source=source, size=10, fill_alpha=0.9)

    # Show the plot
    p = gridplot([[p1, p2]])
    show(p)


# ...
