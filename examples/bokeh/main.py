"""
Geometric patterns and bokeh.

Write a standalone servable Bokeh app that draws exciting geometric patterns.

To run: `$ bokeh serve --show bokeh_spirograph.py`

Inspiration: https://github.com/bokeh/bokeh/blob/branch-2.4/examples/app/sliders.py
and https://demo.bokeh.org/sliders.

"""

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
import numpy as np


def make_values(n, m):
    """Make (x, y) values for the plot."""
    t = np.linspace(0, m*n, n)
    r = t % n
    x = r * np.sin(t)
    y = r * np.cos(t)
    return x, y


def update_values(attrname, old, new):
    """Update the plot based on new inputs."""
    # Get the current slider values.
    n = set_n.value
    m = set_m.value

    # Generate new values from updated inputs.
    x, y = make_values(n, m)

    ds.data = dict(x=x, y=y)


# Initial values and data source for the plot.
n = 1000
m = 2
x, y = make_values(n, m)

ds = ColumnDataSource(data=dict(x=x, y=y))

# Interactive sliders.
set_n = Slider(title="n", value=100, start=10, end=1000, step=5)
set_m = Slider(title="m", value=2, start=1, end=20, step=1)

# Link sliders to plot so that changing the sliders changes the plot.
for slider in [set_n, set_m]:
    slider.on_change('value', update_values)

# Create and show the plot and sliders (that is, the dashboard).
plot = figure(height=500, width=500, title="Spirograph", name="plot")
plot.line('x', 'y', source=ds, line_width=2)

widgets = column(set_n, set_m)
curdoc().add_root(row(widgets, plot, name="plot"))
curdoc().title = "Spirograph"