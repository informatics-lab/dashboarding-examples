# Voilà Examples

An example Jupyter notebook that can be rendered as a simple dashboard using [Voilà](https://voila.readthedocs.io/).

## Overview

Voilà is a custom static Jupyter notebook renderer that retains interactive and output elements of the rendered notebook. This means that markdown cells and code cell outputs (including printed results and displayed objects such as images and figures) will be displayed in the voilà-rendered notebook. 

Interactive elements can also be rendered - but only if they do not rely on their own server for interactivity. This makes [ipywidgets](https://ipywidgets.readthedocs.io/) a good match for interactive elements in notebooks rendered by voilà, as they run in the notebook's own JavaScript frontend. It also means other dashboarding technologies featured in this repo by and large are not compatible with voilà.

This example, then, makes an interactive spirograph plot in a Jupyter notebook using sliders from ipywidgets to interactively modify a plot that is drawn with matplotlib. The sliders are bound to a callback function that fires on slider change and re-draws the plot from the latest values set with the sliders. The plot itself is interactively rendered in the notebook using [ipympl](https://github.com/matplotlib/ipympl).

## Usage

To render this example notebook using voilà:

```bash
$ voila voila_spirograph.ipynb
```

Note that the sliders and plot elements will take a little longer to show than the text and heading elements of the rendered notebook.

## Python Environment

To run this demo you will need a Python environment containing `voilà` and `NumPy`. For example:

```bash
conda install -c conda-forge numpy voila
```